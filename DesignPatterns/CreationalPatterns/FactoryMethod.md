# Factory
- At the core of the Factory Method pattern is the concept of delegation. Instead of the client code directly creating objects, it delegates the responsibility to a Factory Method.
- The design pattern Factory resolves the problem when you work with a few classes following the same interface. As a user of the interface, you are not interested in the implementation details of a certain class.
- Your goal is to have an instance that serves your needs.

The Factory Method pattern recommends encapsulating the functionality required, to select and instantiate an appropriate class, inside a
designated method referred to as a factory method. Thus, a factory method can be deﬁned as a method in a class that:
- Selects an appropriate class from a class hierarchy based on the application
context and other inﬂuencing factors
- Instantiates the selected class and returns it as an instance of the parent
class type.

##  Step 1: Define the Product Interface
First, we define a simple interface for our products, in this case, pets. Each pet will have a method speak.

```sh
class Pet:
    def speak(self):
        pass
```

## Step 2: Create Concrete Products
Next, we create concrete classes that implement the Pet interface.

```sh
class Dog(Pet):
    def speak(self):
        return "Woof!"

class Cat(Pet):
    def speak(self):
        return "Meow!"
```

## Step 3: Implement the Factory
Now, we create the factory class or method that will be used to instantiate the pets.

```sh
class PetFactory:
    @staticmethod
    def get_pet(pet_type: str) -> Pet:
        pets = dict(dog=Dog(), cat=Cat())
        return pets.get(pet_type, None)
```

## Step 4: Use the Factory
Finally, we use the factory to create pet instances without directly invoking the constructor of the Dog or Cat classes.

```sh
if __name__ == "__main__":
    pet_type = input("Which pet would you like? (dog/cat): ")
    pet = PetFactory.get_pet(pet_type)
    if pet:
        print(f"Your pet says: {pet.speak()}")
    else:
        print("Sorry, we don't have that pet.")
```

## Advanced examples 

### Mysql-utilities

```sh
   24 """Implementing support for MySQL Authentication Plugins"""
   25 
   26 from hashlib import sha1
   27 import struct
   28 
   29 from . import errors
   30 from .catch23 import PY2, isstr
   31 
   32 
   33 class BaseAuthPlugin(object):
   34     """Base class for authentication plugins
   35 
   36 
   37     Classes inheriting from BaseAuthPlugin should implement the method
   38     prepare_password(). When instantiating, auth_data argument is
   39     required. The username, password and database are optional. The
   40     ssl_enabled argument can be used to tell the plugin whether SSL is
   41     active or not.
   42 
   43     The method auth_response() method is used to retrieve the password
   44     which was prepared by prepare_password().
   45     """
   46 
   47     requires_ssl = False
   48     plugin_name = ''
   49 
   50     def __init__(self, auth_data, username=None, password=None, database=None,
   51                  ssl_enabled=False):
   52         """Initialization"""
   53         self._auth_data = auth_data
   54         self._username = username
   55         self._password = password
   56         self._database = database
   57         self._ssl_enabled = ssl_enabled
   58 
   59     def prepare_password(self):
   60         """Prepares and returns password to be send to MySQL
   61 
   62         This method needs to be implemented by classes inheriting from
   63         this class. It is used by the auth_response() method.
   64 
   65         Raises NotImplementedError.
   66         """
   67         raise NotImplementedError
   68 
   69     def auth_response(self):
   70         """Returns the prepared password to send to MySQL
   71 
   72         Raises InterfaceError on errors. For example, when SSL is required
   73         by not enabled.
   74 
   75         Returns str
   76         """
   77         if self.requires_ssl and not self._ssl_enabled:
   78             raise errors.InterfaceError("{name} requires SSL".format(
   79                 name=self.plugin_name))
   80         return self.prepare_password()
   81 
   82 
   83 class MySQLNativePasswordAuthPlugin(BaseAuthPlugin):
   84     """Class implementing the MySQL Native Password authentication plugin"""
   85 
   86     requires_ssl = False
   87     plugin_name = 'mysql_native_password'
   88 
   89     def prepare_password(self):
   90         """Prepares and returns password as native MySQL 4.1+ password"""
   91         if not self._auth_data:
   92             raise errors.InterfaceError("Missing authentication data (seed)")
   93 
   94         if not self._password:
   95             return b''
   96         password = self._password
   97 
   98         if isstr(self._password):
   99             password = self._password.encode('utf-8')
  100         else:
  101             password = self._password
  102 
  103         if PY2:
  104             password = buffer(password)  # pylint: disable=E0602
  105             try:
  106                 auth_data = buffer(self._auth_data)  # pylint: disable=E0602
  107             except TypeError:
  108                 raise errors.InterfaceError("Authentication data incorrect")
  109         else:
  110             password = password
  111             auth_data = self._auth_data
  112 
  113         hash4 = None
  114         try:
  115             hash1 = sha1(password).digest()
  116             hash2 = sha1(hash1).digest()
  117             hash3 = sha1(auth_data + hash2).digest()
  118             if PY2:
  119                 xored = [ord(h1) ^ ord(h3) for (h1, h3) in zip(hash1, hash3)]
  120             else:
  121                 xored = [h1 ^ h3 for (h1, h3) in zip(hash1, hash3)]
  122             hash4 = struct.pack('20B', *xored)
  123         except Exception as exc:
  124             raise errors.InterfaceError(
  125                 "Failed scrambling password; {0}".format(exc))
  126 
  127         return hash4
  128 
  129 
  130 class MySQLClearPasswordAuthPlugin(BaseAuthPlugin):
  131     """Class implementing the MySQL Clear Password authentication plugin"""
  132 
  133     requires_ssl = True
  134     plugin_name = 'mysql_clear_password'
  135 
  136     def prepare_password(self):
  137         """Returns password as as clear text"""
  138         if not self._password:
  139             return b'\x00'
  140         password = self._password
  141 
  142         if PY2:
  143             if isinstance(password, unicode):  # pylint: disable=E0602
  144                 password = password.encode('utf8')
  145         elif isinstance(password, str):
  146             password = password.encode('utf8')
  147 
  148         return password + b'\x00'
  149 
  150 
  151 class MySQLSHA256PasswordAuthPlugin(BaseAuthPlugin):
  152     """Class implementing the MySQL SHA256 authentication plugin
  153 
  154     Note that encrypting using RSA is not supported since the Python
  155     Standard Library does not provide this OpenSSL functionality.
  156     """
  157 
  158     requires_ssl = True
  159     plugin_name = 'sha256_password'
  160 
  161     def prepare_password(self):
  162         """Returns password as as clear text"""
  163         if not self._password:
  164             return b'\x00'
  165         password = self._password
  166 
  167         if PY2:
  168             if isinstance(password, unicode):  # pylint: disable=E0602
  169                 password = password.encode('utf8')
  170         elif isinstance(password, str):
  171             password = password.encode('utf8')
  172 
  173         return password + b'\x00'
  174 
  175 
  176 def get_auth_plugin(plugin_name):
  177     """Return authentication class based on plugin name
  178 
  179     This function returns the class for the authentication plugin plugin_name.
  180     The returned class is a subclass of BaseAuthPlugin.
  181 
  182     Raises errors.NotSupportedError when plugin_name is not supported.
  183 
  184     Returns subclass of BaseAuthPlugin.
  185     """
  186     for authclass in BaseAuthPlugin.__subclasses__():  # pylint: disable=E1101
  187         if authclass.plugin_name == plugin_name:
  188             return authclass
  189 
  190     raise errors.NotSupportedError(
  191         "Authentication plugin '{0}' is not supported".format(plugin_name))
  ```

### Resource Factory
```sh
""" Resource classes for the factory type """
from abc import ABC, abstractmethod

class Resource(ABC):
    """ This Abstract class represents the Resource """
    resource_id = None  # id of concept group, provider group, npi file
    client_id = None
    audience_version_id = None
    credentials = None # credentials of gcp to loggin
    headers = None  # headers
    gcp_bucket_name = None # gcp bucket name to upload files for data ml

    @abstractmethod
    def validate_file_for_resource(self):
        """ This method validates the file for the resource """

    def upload_file_to_gcp(self):
        """ This method uploads the file to GCP """
```

```sh
class ProviderGroup(Resource):
    """ This Abstract class represents the Audience """
    gcp_path_audience_type = None
    url_file_downloaded = None  # url of the file downloaded
    error_code = None  # error code
    gcp_file_name = None  # gcp file name
    pg_version_id = None  # provider group version id


    def __get_active_version_id(self) -> str:
        """ Get the active version id from the concept group """
        self.pg_version_id = get_active_version_from_group(
            get_pg_versions_api_url,
            self.resource_id,
            self.headers,
            "providerGroupVersionId", "_embedded")
        logger.info(f"pg_version_id: {self.pg_version_id}")

    def __get_providers_from_provider_group_version_id(self) -> int:
        """ Get the providers from the provider group version id """
        url_providers = get_pg_providers_from_version_api_url(
            self.resource_id, self.pg_version_id)
        logger.info(f"url_providers: {url_providers}")

        response_providers = requests_request(
            'GET', url=url_providers, headers=self.headers, data={}, timeout=90)
        logger.info("url_providers.status_code: %s",
                    response_providers.status_code)

        return response_providers.status_code

    def __download_file_from_service(self) -> str:
        """ Download the file from the provider groups APIS """
        return download_file.download_providers_from_provider_group(self.gcp_file_name,
                                                                    self.resource_id,
                                                                    self.headers,
                                                                    self.pg_version_id)

    def __validate_file_for_service(self) -> str:
        """ Validate the file from the provider group """
        return validate_files_from_groups.validate_file_from_providergroup(
            self.url_file_downloaded)

    def __upload_file_to_gcp(self) -> str:
        """ Upload the file to GCP """
        folder_name = DagFileNameEnums.PROVIDERGROUP.value
        path_gcs_file_name = FILE_NAME_UPLOADED_FOLDER.format(
            self.gcp_path_audience_type,
            self.client_id,
            self.audience_version_id,
            folder_name,
            self.gcp_file_name)

        upload_file_to_gcp(
            self.error_code,
            path_gcs_file_name,
            self.url_file_downloaded,
            self.gcp_bucket_name,
            self.credentials)
        path_gcs_file_name = f"{GCS}{self.gcp_bucket_name}/{path_gcs_file_name}"
        return path_gcs_file_name

    def validate_file_for_resource(self) -> None:
        """ Validate the file for the resource """
        self.__get_active_version_id()
        status_code = self.__get_providers_from_provider_group_version_id()

        if status_code == HTTPStatus.OK.value:
            self.url_file_downloaded = self.__download_file_from_service()

            if self.url_file_downloaded is not None:
                self.error_code = self.__validate_file_for_service()
        else:
            self.error_code = ErrorCode.EMPTY_FILE_WITH_NO_RESULTS.value

    def upload_file_to_gcp(self)-> dict:
        """ Upload the file to GCP """
        path_gcs_file_name = self.__upload_file_to_gcp()
        return {"provider_group_path": path_gcs_file_name}


    def trasform_resource_id(self)-> dict:
        """ Upload the file to GCP """
        return {"provider_group_id": self.resource_id}
```

```sh
class ResourceFactory():
    """This class represents the Resource Factory."""
    target_implementations = {}

    def __init__(self):
        self.load_target_types()

    def load_target_types(self):
        """Loads the target types into the factory."""
        implementations = getmembers(resource_types, lambda m: isclass(m) and not isabstract(m))

        for name, _type in implementations:
            if isclass(_type) and issubclass(_type, resource.Resource):
                self.target_implementations[name] = _type

    def create(self, target_type: str):
        """Creates an instance of the specified target type.

        Args:
            target_type (str): The name of the target type to create.

        Returns:
            An instance of the specified target type.

        Raises:
            ValueError: If the target type is not supported.
        """
        if target_type in self.target_implementations:
            return self.target_implementations[target_type]()
        else:
            raise ValueError(f"{target_type} is not currently supported as a target type")
```
