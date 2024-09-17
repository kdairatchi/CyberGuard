**CyberGuard: A Customizable and User-Friendly Cybersecurity Tool**
======================
**Introduction**
---------------

CyberGuard is a customizable and user-friendly cybersecurity tool that uses AI to scan networks, detect vulnerabilities, and provide recommendations for improvement.

**Installation**
---------------

1.  Clone the repository: `git clone https://github.com/kdairatchi/CyberGuard.git`
2.  Install the dependencies: `pip install -r requirements.txt`
3.  Create a `data.csv` file with the following format:
    ```
"IP Address","Port","Protocol","Vulnerability"
"192.168.1.1",22,"TCP",1
"192.168.1.1",80,"TCP",0
"192.168.1.1",443,"TCP",1
"192.168.1.2",22,"TCP",0
"192.168.1.2",80,"TCP",1
```
4.  Train the AI model: `python cyberguard.py train data.csv`

**Usage**
-----

1.  Scan the network: `python cyberguard.py scan_network 192.168.1.0/24`
2.  Scan the ports: `python cyberguard.py scan_ports 192.168.1.100 22 80 443`
3.  Detect vulnerabilities: `python cyberguard.py detect_vulnerabilities 192.168.1.100 22 80 443`
4.  Provide recommendations: `python cyberguard.py provide_recommendations 192.168.1.100 22 80 443`

**Troubleshooting**
----------------

*   **Error: No `data.csv` file found**: Create a `data.csv` file with the correct format and train the AI model using the `train` command.
*   **Error: AI model not trained**: Train the AI model using the `train` command and the `data.csv` file.
*   **Error: Invalid IP address or port range**: Check the IP address and port range and try again.

**Updates**
-------

*   To update CyberGuard, run `git pull` in the repository directory.
*   To update the dependencies, run `pip install -r requirements.txt` in the repository directory.

**Customization**
--------------

*   To customize CyberGuard, modify the `cyberguard.py` script.
*   To add new features, modify the `cyberguard.py` script and add new functions or classes.

**Contributing**
------------

*   To contribute to CyberGuard, fork the repository and submit a pull request.
*   To report issues or bugs, create an issue in the repository.

**License**
-------

CyberGuard is licensed under the MIT License.

**Acknowledgments**
---------------

CyberGuard was created by [Your Name] as a project for [Your Course/Company]. Special thanks to [Your Instructor/Colleagues] for their guidance and support.

**References**
--------------

*   [Scapy Documentation](https://scapy.readthedocs.io/en/latest/)
*   [Python Documentation](https://docs.python.org/3/)
*   [Tkinter Documentation](https://docs.python.org/3/library/tk.html)
*   [PyQt Documentation](https://doc.qt.io/qtforpython/)
