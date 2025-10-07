import requests
import json
import pandas as pd
import os
import joblib
import time
start = time.time()
links ={'Bandwidth vs. Throughput vs. Latency _ Computer Networks': 'https://youtu.be/cDVNU2j26Bs?si=9yvXCX4B8sCyy0NE', 'Basics of Communication _ Computer Networks': 'https://youtu.be/kon5GS_OWl4?si=_p6n3lyyJgclgw0E', 'Fast Ethernet vs. Gigabit Ethernet with examples _ Computer Networks': 'https://youtu.be/V1y8fkNWp8c?si=FSsafDkgOu9Ee9yT', 'LAN, MAN, WAN, PAN , CAN _ Computer Networks': 'https://youtu.be/n0iaPtsnmxQ?si=AyMEzZZVdVEUcSvj', 'Lec-10_ Repeaters in Computer Networks _ Physical layer devices': 'https://youtu.be/mf4bRP_puNQ?si=aAvyu_DISGkrgKkI', 'Lec-11_ Hub in Computer Networks _ Physical layer devices': 'https://youtu.be/3N5a9cHYzCM?si=NjzWHcv_RV2sTl8O', 'Lec-12_ Bridges In Computer Networks _ Physical and data link layer device': 'https://youtu.be/dDP36_ZBs6A?si=LwO0IEeDYqYo6Gnj', 'Lec-13_ Switch, Hub & Bridge Explained - What s the difference ': 'https://youtu.be/vdtqEPKYB5M?si=rInWQVv8c0aTS2Ch', 'Lec-14_ Routers in Computer Networks _ Physical, data link and network layer device': 'https://youtu.be/JhBnOamc_8s?si=576WN-bLhioMl6Jr', 'Lec-15_ Collision Domain Vs. Broadcast Domain _ Repeater, Hub, Bridge, Switch, Router _ Networks': 'https://youtu.be/301XUVtn-6s?si=L8m0wN8VM30jBfu6', 'Lec-16_ What is Circuit Switching in Computer Networks in Hindi': 'https://youtu.be/Cug52cpjM_g?si=JYZEfx-QbnJzsgV3', 'Lec-17_ Packet Switching In Computer Networks _ Imp for GATE and UGC NET': 'https://youtu.be/_0mE6PH1E4c?si=SXQrpbqtgVjX0ZOm', 'Lec-18_ Datagram Switching Vs Virtual Circuit Switching in Packet Switching _ Computer Networks': 'https://youtu.be/-S-NThI_79o?si=vx7irOWaZuDGWeRb', 'Lec-19_ What is Message Switching In Computer Networks': 'https://youtu.be/T1rSrLPHLLI?si=RaP1cs8oEcpslpv7', 'Lec-1_ Computer Networks and Security Full Syllabus for GATE, UGC NET,DSSSB,NIELIT & University exam': 'https://youtu.be/JFF2vJaN0Cw?si=IUSjsjnWYY7pDwPb', 'Lec-20_ Unicast, Broadcast & Multicast in Computer Networks': 'https://youtu.be/EcWhJbEWxHU?si=RuIbCRXA_MJeXQ2_', 'Lec-21_ Data link layer in computer Networks and its Responsibilities': 'https://youtu.be/JRgmPco0KWI?si=KNpoFz0ovgpKzaCp', 'Lec-22_ Stop and Wait ARQ protocol _ Data link layer': 'https://youtu.be/YIX1NfaUpsU?si=O1c-KZpYGXwGUmAq', 'Lec-23_ Go-Back-N ARQ (Automatic Repeat Request) _ Data Link layer': 'https://youtu.be/zc88y9HTAOA?si=HUAWugqlQDGwqSTR', 'Lec-24_ Selective Repeat ARQ (Automatic Repeat Request) _ Data Link Layer': 'https://youtu.be/08y_Vrs1vHo?si=JxY82EIiGntKbH_M', 'Lec-25_ Various Flow Control Protocols _ Stop&Wait , GoBackN & Selective repeat in Data Link Layer': 'https://youtu.be/yNedVgNyE8Q?si=lAYmkvh2gG3hR0f-', 'Lec-26_ Framing in Data Link Layer _ Bit Stuffing vs Byte(Character) Stuffing': 'https://youtu.be/2U6kPu0dfqI?si=oaXzdlEIjL9iOWoC', 'Lec-27_ Introduction to Error detection and Correction _ Computer Networks': 'https://youtu.be/U7-h2hyM1Dc?si=ZbeL_Sh7lC_pR2HA', 'Lec-28_ Single Bit Parity along With Hamming Distance Concept _ Error Control': 'https://youtu.be/U09cNsiYpc8?si=b23PTcUPjX3b64XN', 'Lec-29_ Cyclic Redundancy Check(CRC)  for Error Detection and Correction  _ Computer Networks': 'https://youtu.be/5Q-Yv6_0Qcw?si=v5EjFmgRajFEPJyP', 'Lec-2_ Introduction to Computer Network _ OSI MODEL in easiest Way in Hindi _ Need of OSI model': 'https://youtu.be/4D55Cmj2t-A?si=SgXh5K_HI2GOT8VG', 'Lec-30_ Hamming Code for Error Detection & Correction both with easiest examples': 'https://youtu.be/V5Iu52tbZEQ?si=8iizww6xrSHuBubS', 'Lec-31_ Various Medium Access Control Protocols in Data Link Layer _ Computer Networks': 'https://youtu.be/G0h0dC4Zycs?si=UDo1_eeFsO0W4vVN', 'Lec-32_ What is Pure Aloha in Hindi _ MAC Layer Protocol': 'https://youtu.be/WYM9nFYnYAg?si=sK8jSBCt54FeOyca', 'Lec-33_ Pure Aloha Vs Slotted Aloha with all imp points in Hindi _ Computer Networks': 'https://youtu.be/ggdeb2_z240?si=g7NgCdrEbY9wAX5k', 'Lec-34_ Carrier Sense Multiple Access in Computer Network __ CSMA __ Computer Networks': 'https://youtu.be/IftFvfSywCQ?si=s-4_8UMKeOKSTcXc', 'Lec-35_ Carrier Sense Multiple Access_ Collision Detection _ CSMA_CD _ Computer Networks': 'https://youtu.be/v_z888gQWq0?si=q6Ioft8QGrQjldRJ', 'Lec-36_ CSMA_CA in Computer Network _ Full Explanation': 'https://youtu.be/reQ938TeFHM?si=xrJIB1m6RdxiWNrw', 'Lec-37_ GATE Question on CSMA_CD _ GATE-2015': 'https://youtu.be/oNOVfVcWBXc?si=lkA1gjrIGjfHDccK', 'Lec-38_ Ethernet Frame Format (IEEE-802.3) in Data Link Layer': 'https://youtu.be/ewpq3qxx5Ls?si=6IAiVYm3lkStL4YH', 'Lec-39_ Token Ring (IEEE 802.5) in Computer Networks': 'https://youtu.be/-u4Dzu63eZc?si=Eg3wDGbSMj0ymLJt', 'Lec-3_ TCP_IP Protocol Suite _ Internet Protocol Suite _ OSI vs TCP_IP': 'https://youtu.be/GfaHdjApnhU?si=OmY2jZEsjyeOhaKk', 'Lec-40_ Network Layer _ Responsibilities of Network Layer _ OSI Model _ Computer Networks': 'https://youtu.be/rW1jPlYgp_0?si=oJ7bLWfsr0GCW1IU', 'Lec-41_ Class A in IP addressing with Example in HINDI _ Classful Addressing _ Network Layer': 'https://youtu.be/iurle2xZrBQ?si=y3mkgjYKiep7W8t3', 'Lec-42_ Class B in IP addressing with Example _ Classful Addressing in hindi with most easiest way': 'https://youtu.be/es1NEZbgCss?si=q7UAyq5yRc1rG7pE', 'Lec-43_ Class C in IP addressing with Example _ Classful Addressing _ Network Layer': 'https://youtu.be/gk7c-Dceg5Y?si=Q3HC0VfiLqlssh-A', 'Lec-44_ Class D & Class E in IP addressing with Example _ Classful Addressing _ Network Layer': 'https://youtu.be/NDG2SEi2dKo?si=l6v7qZrmy9oam0CQ', 'Lec-45_ Find Range, Network Id, Host, Broadcast address with Numerical Examples in Hindi': 'https://youtu.be/vTzrn_M77mo?si=pV09ve3XSXyz_Dms', 'Lec-46_ Disadvantages of Classful Addressing _ IP addressing _ Computer Networks': 'https://youtu.be/ARfwnD6X6ZI?si=lkflOy6FSK1e3wsz', 'Lec-47_ What is Classless Addressing (CIDR) in Hindi _ CIDR vs Classful Addressing': 'https://youtu.be/N-ywmOpWehE?si=kFHsrzcjFeHnT3LI', 'Lec-48_ Subnetting in Classful Addressing with Examples in Hindi _ Computer Networks': 'https://youtu.be/rdb2ki4iGuo?si=7hwmYdvmrP9qLSUb', 'Lec-49_ Variable Length Subnet Masking(VLSM) in Hindi with Examples _ Computer Networks': 'https://youtu.be/mhVATrk0OhU?si=ZsJL6Wl0eO6oS1oR', 'Lec-4_ Physical layer in computer networks in hindi _ Functions of Physical layer _ OSI': 'https://youtu.be/lg-f92uY1Lc?si=ID-VNIqF9kbcEPOm', 'Lec-50_ Subnetting in CIDR Addressing _ Classless Interdomain Routing in Hindi with Example': 'https://youtu.be/wvvoT-dpr8o?si=ARG9K2qlWHUHQC8t', 'Lec-51_ Numerical Question on CIDR _ Classless Addressing _ Very Imp for all Competitive Exams': 'https://youtu.be/jXioURQ2v8E?si=MU1ztX9ip3NYAP2N', 'Lec-52_ VLSM in Classless Addressing(CIDR) _ Variable Length Subnet Masking': 'https://youtu.be/DFjz3yxe3aU?si=4LfNxmYjYZRkpnlC', 'Lec-53_ IPv4 Header Format – All Fields Explained in Hindi _ Computer Networks': 'https://youtu.be/zoFSxIuS5Ro?si=0j4Q4iTeRA46HM_V', 'Lec-54_ Fragmentation of IPv4 Datagram _ Identification, Flags and Fragment Offset _ Networks': 'https://youtu.be/k8VgrqDOIUo?si=aooLaV1-xnU3CXwH', 'Lec-55_ Options & Padding in IPv4 Header _ Computer Networks': 'https://youtu.be/W1UzRlh1gNc?si=lSM7reiVM6TSuZND', 'Lec-56_ IPv6 Header Format in Hindi _ IPv4 Vs IPv6 in Computer Networks': 'https://youtu.be/U3rGOTxwXAI?si=wWe2qaMzOmA-hgor', 'Lec-57_ What is Routing Protocols _ Various types of Routing Protocols': 'https://youtu.be/rA0p0ouD3aE?si=A8IQWTS4aDgjdmYz', 'Lec-58_ Distance vector routing algorithm in hindi _ Computer Networks': 'https://youtu.be/5ZuP5qjbKSI?si=5Wu3BEz_qxCKoUg8', 'Lec-59_ Count to Infinity Problem in Distance Vector Routing': 'https://youtu.be/UYASPR4jEkk?si=i4j18l6RGnDgMP54', 'Lec-5_ Topologies in Computer Networks _ Part-1 _ All imp points of Mesh, Star, Hub, Bus, Hybrid': 'https://youtu.be/uDulBxDb7GM?si=R4GtkChvZ_iNCT6m', 'Lec-60_ Link state routing in computer networks in Hindi': 'https://youtu.be/kW6zV-040SY?si=Xu4ZtH_gHiLQ8r5p', 'Lec-61_ ARP Explained- Address Resolution Protocol _ Network Layer': 'https://youtu.be/IUSyV2BVh4A?si=tT7c2Xr00ze2aVeS', 'Lec-62_ NAT Explained - Network Address Translation with example in Hindi': 'https://youtu.be/47PUj7OSGkA?si=Fe-G6q3CDGUxFOul', 'Lec-63_ Transport  Layer _ Responsibilities of Transport  Layer _ OSI Model _ Computer Networks': 'https://youtu.be/kAty4mKczEg?si=O0YASU1oCGfEnAtj', 'Lec-64_ TCP_ Transmission control protocol _ TCP Header _ Transport layer _ part -1': 'https://youtu.be/c8aet11HNxg?si=88VEIgm_f8tL_X2Z', 'Lec-65_ TCP_ Transmission control protocol _ TCP Header _ Transport layer _ part -2': 'https://youtu.be/hsNuqtfxgRI?si=F8orhsgU00ONqcJ4', 'Lec-66_ TCP connection Establishment and connection Termination _ Transport layer': 'https://youtu.be/qIEHUUt2Wfc?si=05m1D0VKJt0OCxiB', 'Lec-67_ TCP Data Transfer _ Piggybacking & Pure Acknowledgement': 'https://youtu.be/7zPfuIf4GL0?si=fDsSF0jYFxhEnAQv', 'Lec-68_ Connection Termination in TCP in Hindi with example': 'https://youtu.be/dJIAComFq9U?si=uWkr7G3SKIvuZr4N', 'Lec-69_ TCP Congestion Control in Computer Networks in Hindi': 'https://youtu.be/0bc_T_pEZmo?si=_ZElXEKf_vm65pxo', 'Lec-6_ Topologies in Computer Networks _ Part-2 _ All imp points of Mesh, Star, Hub, Bus, Hybrid': 'https://youtu.be/7t0YJWTjmdI?si=7QZbMGiVtHZCg0Mo', 'Lec-70_ UDP (User Datagram Protocol) header in Computer Networks in Hindi': 'https://youtu.be/HF_znV8x9a0?si=_NwvttTbmXJo0NP1', 'Lec-71_ Advantages of UDP protocol over TCP _ Transport Layer': 'https://youtu.be/Zs0VixZqgzA?si=v6dCf-Crkkt1dUHZ', 'Lec-72_ TCP vs UDP differences in hindi': 'https://youtu.be/jJyXpMmXJI0?si=exbrdgqLu8Kr8xlw', 'Lec-73_ Session Layer of OSI model _ Session layer functions in Hindi': 'https://youtu.be/2Abjxmp7TfU?si=cQmnD04eagoO_OnY', 'Lec-74_ Presentation layer in computer networks in Hindi _ OSI Model': 'https://youtu.be/cj4OxZRJUdw?si=kytfreeloe2jXN3D', 'Lec-75_ Application layer of OSI model in Hindi _ Application layer protocols & Port no': 'https://youtu.be/8An0dRalJeM?si=9Vieqy-x_9aNs0og', 'Lec-76_ Domain Name System (DNS) in computer Networks': 'https://youtu.be/vhfRArT11jc?si=bCDzfQ0PjjaYVzjW', 'Lec-77_ Domain Name Server(DNS) & its types in Hindi _ All about DNS': 'https://youtu.be/BZISxpdl4lQ?si=1-FbiV8tauJo98iK', 'Lec-78_ HTTP, FTP, SMTP, POP _ All Application Layer Protocols _ Computer Networks': 'https://youtu.be/pnoWCK82apU?si=MObrByMOA4BVkGGF', 'Lec-79_ Persistent vs Non-Persistent HTTP _ HTTP_1.0 vs HTTP_1.1': 'https://youtu.be/zRUdSu3JlK8?si=2_d-7yAhnezHQOzd', 'Lec-7_ Manchester encoding and differential Manchester encoding in Hindi _ Computer Network': 'https://youtu.be/3IaB2a8tXLA?si=6flM3--1fZm3Uevr', 'Lec-80_ Cryptography in computer network in Hindi _ Cryptography in Information Security': 'https://youtu.be/trHox1bN5es?si=KvcENnIvmQJqSdEC', 'Lec-81_ Symmetric Key Cryptography in Network Security with examples': 'https://youtu.be/6AmmQiOWoXM?si=y2Bw6a35ZpMxav1_', 'Lec-82_ Imp Question on Network Security _ Symmetric Key Cryptography': 'https://youtu.be/JUi2x_WbVO0?si=TZgZS-Lr00tpeDWO', 'Lec-83_ Asymmetric key Cryptography with example _ Network Security': 'https://youtu.be/xw19eT5thIE?si=DYnZDLzaSQKRFT28', 'Lec-84_ RSA Algorithm in Network Security with examples in Hindi rsa algorithm example in hindi': 'https://youtu.be/VUxfDCmWM0U?si=hKRCJPrdukOkjBYj', 'Lec-85_ What is Firewalls and How it Works _ Packet Filtering firewall explained in Hindi Part-1': 'https://youtu.be/o_vyfo3Hw0Y?si=hcBDXtHU1GmHezO1', 'Lec-86_ What is Application(Proxy) Firewall in Hindi _ Network Security Part-2': 'https://youtu.be/CHtTLireUCA?si=KkvREL5WPf_KMynQ', 'Lec-87_ 3 Imp Questions on Computer Networks_ Must Watch _': 'https://youtu.be/DujE2sRVpeY?si=YsC_okw6pL-pvdem', 'Lec-88_ All Networking Protocols & Devices _ Summary from Physical to Application Layer protocols': 'https://youtu.be/aUYwx9bYlGY?si=ALgBcOq6K8sInjK0', 'Lec-89_ Top Linux Network Commands _ Computer Networks': 'https://youtu.be/Ovm-qqdPKn8?si=KP27ryCQkZQDNrdS', 'Lec-8_ Various Devices In Computer Networks _ Hardware and Software Devices _ Communicating devices': 'https://youtu.be/YxyLN3N5w9s?si=-0U7r3lhPvf1mBrS', 'Lec-90_ Socket Programming in Computer Networks': 'https://youtu.be/XTVTlEhGS6w?si=YJ1Ji5xmvqL_1Iu8', 'Lec-91_ Need of IPv6 Protocol _ Why IPv6 is Required': 'https://youtu.be/0os5MOAKRL0?si=3E0SVXX_uFJ16_rQ', 'Lec-92_ What is IPSec Protocol _ IPsec Introduction _ Computer Networks': 'https://youtu.be/XsgVqrcP32U?si=SKWJdnIVXrr1aIrM', 'Lec-9_ Types Of Cables in Computer Networks _ Coaxial, twisted pair, fibre optic cable': 'https://youtu.be/wuI6FGsOFZU?si=vXmmjEmuUGgbEWPM', 'SMTP vs POP3 vs IMAP with real life example _ All in 1 _ Application layer Protocols': 'https://youtu.be/cjPVlxmf_Vk?si=P17eMkUWV0SWR0mV', 'Transport Mode Vs Tunnel Mode in IPSec _ Computer Networks': 'https://youtu.be/dTkIs9XR4P0?si=AGgiQrqp1Woph7Hv', 'What is Ping📱& Loopback🔁 in Network _ Computer Network': 'https://youtu.be/78hvo-30ayg?si=EGNq2SJ16aWnHA2g', 'Why both IP & Port address is used for Connection _ What is Socket Address with real life example': 'https://youtu.be/zddG06-1Fl0?si=-nuPQ-BDfeB63JgK'}

def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed",json={      # ollama api key : local instance of ollama runs on 11434 port 
        "model":"bge-m3",                                            # select model to create embeddings
        "input":text_list                                            # string to create embedding of
    })

    return r.json()["embeddings"]


# Grouping 5 chunks to 1 :
os.makedirs("json2",exist_ok=True)
files = os.listdir("json")


for file in files:
    with open (f"json/{file}","r") as f:
        data = json.load(f)

    new_chunks=[]
    chunks = data["chunks"]
    text=""   
    start=""
    video_name=""


    for i,chunk in enumerate(chunks):
        
        if i%5==0:
            start =chunk["start"]
            text=""

        video_name = chunk["vid_name"]
        text+=chunk["text"] + " "

        if (i%5==4) or (i==len(chunks)-1):
            new_chunks.append({"start":start,"video_name":video_name,"text":text.strip()})
          

    print(f"for video : {file}")
    print(f"before chunks: {len(data['chunks'])} after chunks : {len(new_chunks)}")        
            
    with open(f"json2/{file}","w") as f:
        json.dump({"chunks":new_chunks},f,indent=4)       
         
# Embedding text
files2 = os.listdir("json2")
dataframe = []

for file in files2:
    print(f"{file}")
    

    with open (f"json2/{file}") as f:
        json_file = json.load(f)
    # print(type(json_file))    

    print(f"embedding {file}")    
    # embedding = create_embeddings([c["text"] for c in json_file["chunks"]])
    # print(embedding) 
    # break    

    embeddings = create_embeddings([c["text"] for c in json_file["chunks"]])

    for i,chunk in enumerate(json_file["chunks"]):
        chunk["embedding"] = embeddings[i]
        chunk["link"] = links[f"{file.split('.mp')[0]}"]
        dataframe.append(chunk)
    

# Saving to joblib file
df = pd.DataFrame.from_records(dataframe)
joblib.dump(df,"embeddings.joblib")

end= time.time()
print(f"time requird : {end-start} seconds")
print(dataframe[0])