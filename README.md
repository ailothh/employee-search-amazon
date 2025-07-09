# Employee Search Tool — Public Version

**Version:** 1.0.0  

 **Note:** Use the **Vercel-hosted version** linked in the *About Me* section.
 
 **Test Input:** `alex winkler`

I am in no way associated with this breach and all breached data has been removed from this public version and replaced with demo data. 

Development on this project has been **formally discontinued** following a direct communication from **AWS Security**.
A selection of this data — including that of VPs and principal engineers — was independently verified and still active as of **June 2025**. This mirrors real-world attacks like the **2020 Twitter hack**, where attackers exploited internal access through social engineering.

As a result:

- All breached data has been removed  
- No further development or updates will be made  
- The repository remains for **transparency and awareness only**
- 
##  Potential for Exploitation

The current implementation allows only name-based lookups. A more advanced — and more dangerous — version could enable:

- **Department-based targeting** (e.g. Identity, SRE, or Security teams)  
- **Role-based queries** (e.g. “Principal Engineer”, “Root Access Admin”)  
- **Location-based filters** (e.g. “AWS Seattle HQ”)
- **Linkedin profile integration**

Such functionality would allow attackers to isolate **high-value targets** for spear phishing, vishing, or internal compromise. 


## Overview

The **Employee Search Tool** is a proof-of-concept application demonstrating how leaked corporate data can be queried to identify and target individuals within an organization. It was inspired by the **2023 Amazon employee data breach**, which exposed personal details for over **1.2 million employees**, including:

- Corporate email addresses  
- Office and personal phone numbers  
- Office room numbers and building locations  
- Internal user IDs and position titles  

## Tool Functionality

This tool allows basic search by **first and last name**, returning all associated metadata.

- Identification of employees and their roles  
- Collection of contact and organizational data  
- Mapping of internal reporting structures for targeted phishing  

## Ethical Disclaimer

- This tool contains **no breached or personal data**  
- It is intended **strictly for educational and security awareness purposes**  

##  Final Thoughts

This project illustrates how **minimal technical effort** is needed to weaponize leaked data. Even years after a breach, active contact information can still be found, verified, and exploited.

Organizations must treat data breaches not as isolated events, but as **long-term threats** — especially when attackers can automate and refine their targeting using tools like this.

