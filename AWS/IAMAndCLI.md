# IAM & AWS CLI

## IAM (Identity and Access Management, Global Service): Users & Groups
In AWS you apply the least privilege principle: don’t give more permissions than a user needs.

### IAM Policies 
Define permissions for an action regardless of the method that you use to perform the operation.
inline: only attached to a user

<p align="center">
  <img src="../images/iampolicy.png" width="600">
  <br/>
</p>

### IAM – Password Policy
Strong passwords by default or custom

### IAM MFA (Multi Factor Authentication)
Password + security device. <br/>
Devices: 
- Software devices (Google authenticator, Authy).
- Physical devices (YubiKey, Gemalto, SurePassId).

#### AWS CloudShell: Region Availability
https://docs.aws.amazon.com/cloudshell/latest/userguide/supported-aws-regions.html

### IAM Roles 
Is an IAM identity that you can create in your account that has specific permissions. to AWS Services. You can use roles to delegate access to users, applications, or services that don't normally have access to your AWS resources.

### IAM Security Tools
- IAM Credentials Report (account level) a report that list all your account’s users and the status of their various credentials.
- IAM Access Advisor (user-level):** shows the service permissions granted to a user and when those services were last accessed.

## How cann users access AWS?
- To access AWS, there are three options:
  1. AWS Management Console (protected by password + MFA)
  2. AWS Command Line Interface (CLI): protected by access keys
  3. AWS Software Developer Kit (SDK): for code, protected by access keys.

- Access keys are generated through the AWS Console (users manage their own access keys - don't share your access keys)
  - Access key ID = username
  - Secret Access Key = password

  Example:
    - Access key ID: BOIATZI79MYFY1PWV9W
    - Secret key: QoIETtFgMfSPBzOtIgVb6dWVd23S4RNiJb8gDKqP

### AWS CLI
- A tool that enables you to interact with AWS services using commands in your command-line-shell
- Direct access to the public APIs of AWS services.
- You can develop scripts to manage your resources
- It's open-source https://github.com/aws/cli

<p align="center">
  <img src="../images/awscli.png" width="500">
  <br/>
</p>

### AWS SDK
- AWS Software Development kit (AWS SDK)
- Language-specific APIs (set of libraries)
- Enables you to access and manage AWS services programmatically
- Embedded within your application
- Supports:
  - Javascript, Python, PHP, .NET, Ruby, Java, Go, Node.js, C++
  - Mobile SDKs (Android, iOS)
  - IoT Device SDKs (Embedded C, Arduino)

### AWS CloudShell
AWS CloudShell provides a browser-based shell for managing AWS resources without needing to provision development environments. With CloudShell, you can quickly run commands through a cloud-based shell instead of setting up a local development environment.

With CloudShell, you get a Linux-based shell accessible directly through your browser. This shell comes preconfigured with the AWS CLI, git, Python, and other common tools already installed so you can start using it immediately.

CloudShell is authenticated using your regular AWS credentials and permissions. So you can seamlessly manage resources and run AWS CLI commands without having to configure new credentials or profiles. It also provides access to your specific AWS account so that you can only interact with resources you have permissions for.

To make development easier, CloudShell allocates 500MB of storage space per AWS region. This storage persists only during your active session, providing temporary space for files, downloads, builds, etc. Anything stored here is deleted after your session terminates.

Sessions in CloudShell time out after periods of inactivity to free up resources. The limit is 20 minutes without any activity. This means you can’t use CloudShell for long-running processes, but it works well for short-term administrative tasks, ad hoc commands, and other interactive workflows.

#### Storing data in CloudShell
The temporary storage is allocated at /mnt/efs. This provides high-performance SSD-backed storage optimized for ephemeral workload data. Any files, downloads, builds, caches, etc that only need to exist during an active session can be stored here. When your CloudShell session is terminated, any data in /mnt/efs will be automatically deleted.

For data that needs to persist across sessions, CloudShell provides storage at /mnt/persistent. This slower hard disk drive storage persists independently of any single CloudShell session. Anything stored here will remain in place until explicitly deleted. This is useful for longer-term configuration files, repositories, credentials, scripts, etc that you want to reuse across multiple sessions.