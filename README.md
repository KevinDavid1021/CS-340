**CS 340 Portfolio Submission – Animal Shelter Dashboard**
This repository contains my completed dashboard project and supporting files for CS 340. The project focuses on building a data-driven dashboard using MongoDB, Python, and Dash to support Grazioso Salvare’s rescue operations.

**How do you write programs that are maintainable, readable, and adaptable?**
I focus on separating responsibilities across different parts of the program. In this project, I created a standalone CRUD Python module that handled all database interactions, while the dashboard focused only on displaying and interacting with data. This made the code easier to read and maintain because each component had a clear purpose.

Using the CRUD module was a major advantage because it allowed me to reuse the same database logic without rewriting queries throughout the dashboard. It also made debugging easier since I could isolate issues to either the data layer or the UI layer.

In the future, I could reuse this CRUD module for other applications that require MongoDB integration, such as web apps, analytics dashboards, or internal business tools. I could also expand it by adding validation, logging, or security features to make it more scalable.

**How do you approach a problem as a computer scientist?**
I approach problems by first breaking down the requirements into smaller, manageable parts. For this project, I started by understanding the database structure and the specific filtering requirements from Grazioso Salvare. Then I built the backend connection before moving into the dashboard interface.

This project felt more realistic compared to previous assignments because it required connecting multiple components together instead of solving isolated problems. I had to think about how data flows between systems, not just how to write code.

In the future, I would continue using this structured approach by:

Clearly defining requirements first
Designing the data model early
Building modular components
Testing each part before integrating everything together

**What do computer scientists do, and why does it matter?**
Computer scientists design and build systems that help organizations make better decisions using data. In this project, I created a dashboard that allows users to filter and visualize animal data quickly, which can directly impact rescue operations.

This type of work matters because it improves efficiency and accuracy. Instead of manually searching through data, organizations like Grazioso Salvare can use tools like this dashboard to instantly identify suitable animals for specific rescue missions.

By building systems that organize and present data effectively, computer scientists help companies save time, reduce errors, and make more informed decisions.

**Project Impact**
This dashboard demonstrates how data-driven tools can support real-world decision-making. It provides an interactive way to explore animal shelter data and apply filters based on rescue criteria, making the selection process faster and more efficient.
