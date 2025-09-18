# IT5016-Assessment-3 Programming Principles and Concepts

# Overview

This project is Python Requisition System.
It enables employees to generate requisitions, calculates the overall costs, and oversees the approvals.
Managers are then able to act on requisitions later on and the system gives statistics of the overall submissions.
This repository shows how the idea and concepts of programming can be used to ensure that the code is more maintainable, extendable, and readable.

## Code Contents

	UjjwalBharati_Assignment2-PartB.py - Python program.

### Includes:

    - User input handling
    - Checking of dates, staff IDs, names and item prices.
    - Id generation of requisition automation.
    - Approval logic
    - Manager response
    - Statistics display

### Program Design
*	Class

        Manages creation, validation, total and approval status of requisitions.
*	Data stored in advance (requisitions list)

        Stores all the requisitions in the memory.
*	Menu function

        Gives navigation to make requisitions, all the requisitions, statistics, and responds as a manager.

## Software Development Principles Implemented.

In this project, a number of software engineering concepts are incorporated:
* K.I.S.S (Keep It Simple, Stupid)

        Validation logic and user input are easy.

        Simple threshold (below $500 = approved) is used in approval logic.
-  D.R.Y (Don't Repeat Yourself)
        
        Input validation loops are also of the same reusable structure (check if empty, check type).

        One responsibility is assigned to one object.

* Single Responsibility Principle (SRP)
    
      One concern is dealt with by each method:
        -	init: Gathers information and sums up.
        -	respondrequisition: MV manager responses.
        -	displayall: Shows the details of requisition.
        -	statistics: shows the statistics.

* Separation of Concerns

        This is a business logic in the class.
        Menu() This is a function that is used to interact with the user.
* Open/Closed Principle

        Extension (new item types, additional validation, persistence) does not require a change in the fundamental design.
* Composition instead of Inheritance.

        Instead of using its useless heritage, requisitions are stored as objects within a list.
* Y.A.G.N.I (You Aren't Gonna Need It)

        Only needed features (input, approval, statistics) are done.
        None of premature database integration or additional complexity.
* Clean Code > Clever Code

        Use descriptive identifiers (totalprice, requisitions) as opposed to abbreviated identifiers.
        Logic that can be easily followed step by step.

## Reflection

This source illustrates the ability to design software using programming concepts to achieve a solution that is:

        	Intuitive (Clean Code, KISS)
        	More easily extended and maintained (Open/Closed, SRP, Separation of Concerns)
        	Not duplicated, over-complicated (DRY, YAGNI)
Another way that the project demonstrates the development of procedural code into an OOP design is that it leads to clarity and organization.

## Future Improvements

    -	Store requisitions in a file (CSV/JSON) so that they can be saved.
    -	Provide more rigid date and staffID formats checking.
    -	Implement role based menus (staff vs manager)
    -	Include additional statistics (average value of requisition, maximum/minimum requisition)
