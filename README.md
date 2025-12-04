# SS1100: Intro to Programming for Space Applications
## Final Project: Programming Spacecraft Systems

This repository contains the starter code and resources for the SS1100 Final Project. The goal of this project is to apply your programming skills to solve a variety of problems related to spacecraft subsystems.

### Project Structure

The project is organized into folders, one for each spacecraft subsystem:

- **/RCS/**: Reaction Control Subsystem
- **/TCS/**: Thermal Control Subsystem
- **/ADC/**: Attitude Control Subsystem (Note: ADC is used in the folder name for brevity)
- **/C&DH/**: Command and Data Handling
- **/EPS/**: Electrical Power Subsystem
- **/Payload/**: Remote Sensing Payload

Each folder contains the necessary scripts and data files for that subsystem's tasks.

### Getting Started

For each subsystem, you will find a primary Python script (e.g., `rcs_script.py`, `thermal_control.py`, etc.). Your task is to complete the functions within these scripts according to the instructions in the main project document (`Final Project Instructions.pdf`).

### Verifying Your Code with Unit Tests

Each subsystem folder also contains a `/test` directory with a unit test script (e.g., `test_rcs.py`). These tests are designed to help you verify that your code is working correctly.

To run the tests for a specific subsystem, navigate to that subsystem's directory in your terminal and run the test script. For example, to test your RCS code:

```bash
cd RCS
python test/test_rcs.py
```

If your functions are implemented correctly, the tests should pass without errors.

### Capstone: Mission Simulation

Once you have completed the tasks for all the individual subsystems, you can tackle the final capstone challenge in `mission_simulation.py`. This script, located in the root directory, is designed to integrate the functions you've written into a single, cohesive mission sequence.

---

## Questions for Writeup

*Answer the following questions here, replacing this text with your group's responses.*

1.  **What was your experience in collaborating?** Talk about what steps you used to ensure the inputs from group members worked - code testing, GitHub branch management, etc. - and how you divided up the workload for the project.
   
2.  **What was the most challenging section, and why?** Feel free to provide more than one response if there is a difference of opinion in the group.
   
3.  **If you employed Generative AI tools, how did you do so?** Discuss which tools you used, the prompts you utilized, how you ensured the results were valid, and how you integrated the code into your tasks.
  
4.  **What other resources did you use to find solutions?** Online sites, books, references, etc.
  
5.  **In what way could this project be improved for future quarters?**
