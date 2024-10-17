# SOLID

## Before jumping into SOLID principles Let’s understand coupling and cohesion.
Coupling if two modules’ responsibilities overlap in some way, then a single change may well affect them both. We can measure this overlap by measuring the probability that a modification to one module will propagate to the other. This is called coupling, and high coupling is an enemy of modifiability.

<p align="center">
  <img src="images/coupling.png">
  <br/>
</p>

Cohesion: Cohesion measures how strongly the responsibilities of a module are related. High cohesion is good and means that the class is focused on what it should be doing; low cohesion is bad and means that the class does a great variety of actions.

<p align="center">
  <img src="images/cohesion.png">
  <br/>
</p>

### SRP: THE SINGLE RESPONSIBILITY PRINCIPLE
Of all the SOLID principles, the Single Responsibility Principle (SRP) might be the  least well understood. That’s likely because it has a particularly inappropriate name. It is too easy for programmers to hear the name and then assume that it means that every module should do just one thing.

<p align="center">
  <img src="images/srp.png">
  <br/>
  <i>"A module should be responsible to one, and only one, actor"</i>
</p>

This class violates the SRP because:
    - those three methods are responsible to three very different actors.
    - multiple people changing the same source file for different reasons

The SRP says to separate the code that different actors depend on.


### OCP: THE OPEN-CLOSED PRINCIPLE
<center><i>"A software artifact should be open for extension but closed for modification."</i></center>

Architects separate functionality based on how, why, and when it changes. The goal is to make the system easy to extend without incurring a high impact of change. This goal is accomplished by partitioning the system into components, and arranging those components into a dependency hierarchy that protects higher-level components from changes in lower-level components.

<p align="center">
  <img src="images/ocp.png">
  <br/>
</p>

The Shape class is open for extension as new shapes can be added without modifying its source code, and it's closed for modification as the existing shapes are not altered.

### LSP: THE LISKOV SUBSTITUTION PRINCIPLE

In 1988, Barbara Liskov wrote the following as a way of defining subtypes.

"What is wanted here is something like the following substitution property: If for each object o1 of type S there is an object o2 of type T such that for all programs P defined in terms of T, the behavior of P is unchanged when o1 is substituted for o2 then S is a subtype of T."

it states that objects of a superclass should be seamlessly replaceable with objects of its subclass, without causing any issues or compromising the correctness of the program. This means that a subclass should be able to effortlessly substitute its parent class wherever it is expected.

<p align="center">
  <img src="images/lsp.png">
  <br/>
</p>

A simple violation of substitutability, can cause a system’s architecture to be polluted with a significant
amount of extra mechanisms.

<p align="center">
  <img src="images/lspCode.png">
  <br/>
</p>

To use the LSP effectively, consider the following guidelines:
    1. Maintain the Same Behavior: Derived classes should honor the contracts and behaviors defined by the base class.
    2. Avoid Stronger Preconditions: Derived classes should not have more restrictive requirements (input requirements) than the base class. 

Another example:

<p align="center">
  <img src="images/lspCode2.png">
  <br/>
</p>

<p align="center">
  <img src="images/lspCode3.png">
  <br/>
</p>

### ISP: THE INTERFACE SEGREGATION PRINCIPLE

it is harmful to depend on modules that contain more than you need. This is obviously true for source code dependencies that can force unnecessary recompilation and redeployment—but it is also true at a much higher, architectural level.

<p align="center">
  <img src="images/isp1.png">
  <br/>
</p>

<p align="center">
  <img src="images/isp2.png">
  <br/>
</p>

### DIP: THE DEPENDENCY INVERSION PRINCIPLE

The Dependency Inversion Principle (DIP) tells us that the most flexible systems are those in which source code dependencies refer only to abstractions, not to concretions.

Changes to concrete implementations do not always, or even usually, require changes to the interfaces that they implement. Therefore interfaces are less volatile than implementations.

<p align="center">
  <img src="images/dip.png">
  <br/>
</p>

## DRY, KISS & YAGNI Principles

- **DRY** is about the duplication of knowledge, of intent. It’s about expressing
the same thing in two different places, possibly in two totally different ways.

- **KISS** is an acronym for Keep It Simple, Stupid. This principle says about to make your code simple. You should avoid unnecessary complexity. A simple code it’s easier to maintain and easier to understand.

- **YAGNI** stands for You Ain’t Gonna Need It. It’s a principle from software development methodology of Extreme Programming (XP). This principle says that you should not create features that it’s not really necessary.