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
   Overall, the collaboration effort went well between our group members. Once we got familiar with GitHub, things went pretty smoothly. The biggest sticking point was getting our preferred IDEs to link up with GitHub Desktop. After that was worked out, the confidence of having a commit history helped with rapid editing and committing to the online main. We had three group members, so we just divided up the subsystems with two per member.
2.  **What was the most challenging section, and why?** Feel free to provide more than one response if there is a difference of opinion in the group.
   
3.  **If you employed Generative AI tools, how did you do so?** Discuss which tools you used, the prompts you utilized, how you ensured the results were valid, and how you integrated the code into your tasks.
  We used ChatGPT for both code generation and debugging. Prompts generally worked through each task step wise. The most interesting interaction occured when working on the C_DH subsystem. We simply added in the existing code and the LLM infered what we wanted. Results were confirmed by visual inspection and testing with the provided test scripts. The biggest integration challenge was ensuring that the LLM generated code variables matched the existing code structure.

5.  **What other resources did you use to find solutions?** Online sites, books, references, etc.
   Stack Exchange and Reddit did their usual wonders. Additionally, a regular Google search provided some AI interaction that helped a few times as well. 
  
6.  **In what way could this project be improved for future quarters?**
   Maybe a simple visualization for subsytem effects would help with understanding (RCS, TCS, etc.)
