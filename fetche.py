import requests
description="""
Overview
Drawing from the resounding success of the Great AppSec Hackathon 2021, which boasted an impressive turnout of over 6000 registrations, 5000+ participants, and 700+ finalists nationwide, the Cybersecurity Centre of Excellence (CCoE) , DSCI is thrilled to unveil the forthcoming 2024 edition of the Great Hackathon. Anticipation for this year's event is palpable.

 

The Great AppSec Hackathon - 2024, organized by CCoE, is an endeavor targeting students from diverse academic backgrounds (B.Tech/M.Tech/M.Sc/B.Sc/MCA/BCA). The 2024 edition of the Hackathon is going international and is now open to students from all around the globe!

The initiative's primary objectives are manifold: 

To raise awareness about cybersecurity.
Foster skill development.
Provide employment and internship opportunities for students.
Assist organizations in identifying and attracting top talent.
Enhance the overall cybersecurity landscape within the ecosystem.
As we prepare for this eagerly awaited event, our mission is to cultivate innovation, collaboration, and excellence in the cybersecurity realm, thereby contributing to the collective advancement of technology and security practices across India.

 

Overview of Application Security :
Security is not limited to a few experts. Be it, application developers or infrastructure specialists, knowledge in security and privacy will help them create acceptable applications. With the advent of mobile, there are over 2million apps each on Android and iOS. But an interesting fact is 55% do not make it to the platform as they would have missed the security and privacy consideration while developing the application.

 

Web Applications are a growing focal point for cybercriminals.

The most recent statistics from the Verizon Data Breach Report focusing on the retail sector indicate that web applications are a major target for cybercriminals. Specifically, 70% of breaches in the retail sector originated from web applications.
The whole reason we want to avoid web-based threats is to mitigate the risk of a data breach. The average cost of a data breach is 4.24 million dollars
The risk to business is significant when an application vulnerability is exploited leading to an outage, data breach, or brand degradation.

 

Objectives:

Create awareness on threats and vulnerabilities related to application security.
Gamified approach towards learning, Skill building, and providing internship opportunities for students
Encourage students in Application security and help organizations to attract the right talent.
Boost the cybersecurity quotient in the ecosystem.
Eligibility: 
For INDIAN Participants

Students of all disciplines (B.Tech/ M.Tech/ MCA/ BCA/ B.Sc)
For INTERNATIONAL Participants 

Students of all disciplines
Note: Please register and create a login using your own personal credentials, since the same creds/logins will be used consistently across all rounds, including MCQ and CTF


Guidelines
Please register and create a login using your own personal credentials, since the same creds/logins will be used consistently across all rounds, including MCQ and CTF.
This is an online event.
All Dates and Times are IST.
In addition to published game rules, host site policies and rules apply throughout the competition and must be respected by all members of the competition.
Violations of the rules can be deemed unprofessional conduct if determined to be intentional or malicious by the CCoE operation team. 
Participants should work independently; sharing answers or collaborating with another participant to secure multiple spots is deemed as unprofessional conduct. 
All the traffic is monitored. Any attack on the CTF infrastructure is a violation of game rules and the participants performing the attacks will be eliminated/blocked from the CTF event. 
Decisions of the CCoE operations team are final and binding. 
No extra time will be provided to Competitors who stop work during competition time for nature breaks or for those who break for food and/or drink. The access to the challenges will be revoked once the competition is complete. 
The Credentials for the CTF panel will be provided to the participants prior to the event. 

Prizes
Exciting Prize Pool
INR 10 Lacs and Beyond
Exciting Prize Pool of INR 10 Lacs and beyond.



Access to Internship and Job Opportunities


Participation Certificates
Participation Certificates from CCoE, DSCI (Data Security Council of India) - A NASSCOM Initiative.


Sponsors
Platinum Sponsor
Securin
To fuel every organization in the world with seamless security as a fundamental part of their business.




Collaborators
Ecosystem Partner
Telangana State Cyber Security Bureau (TSCSB)
The Telangana State Cyber Security Bureau (TSCSB) was established in response to the exponential rise in cybercrimes and cybersecurity challenges. ...



International Academic Partners
Sponsor
Cardiff University (UK)
Cardiff University is a public research university in Cardiff, Wales. It was established in 1883 as the University College of South Wales and Monmo...




Hague Centre for Strategic Studies HCSS (Netherlands)
personal

The Hague Centre for Strategic Studies (HCSS) seeks to offer its customers (governments, international institutions and industries) strategic decis...


"""


import requests
import json


try:
    response = requests.post(
        "http://localhost:8000/summary/invoke",
        json={
            "input": {"description": description}
        },
    )
    
    # Check response status and handle accordingly
    if response.status_code == 200:
        try:
            content = response.json()["output"]["content"]
            print(content)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
    else:
        print(f"Error: {response.status_code} - {response.reason}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
