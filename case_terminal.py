#!/usr/bin/env python3
"""
VISAKHAPATNAM (VIZAG) POLICE DEPARTMENT // CENTRAL CRIME STATION
CASE FILE #VIZ-309: THE GITAM UNIVERSITY MURDER
Interactive Fair-Play Homicide Investigation Game
"""

import sys
import time

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
PINK = "\033[95m"
WHITE = "\033[37m"

def print_header():
    print(f"\n{RED}{BOLD}" + "=" * 76 + f"{RESET}")
    print(f"{RED}{BOLD}  VISAKHAPATNAM (VIZAG) POLICE // HOMICIDE DIVISION{RESET}")
    print(f"{YELLOW}{BOLD}  CASE #VIZ-309: THE GITAM UNIVERSITY MURDER (RUSHIKONDA CAMPUS){RESET}")
    print(f"{CYAN}  VIZAG POLICE // HOMICIDE SQUAD // CASE DOSSIER{RESET}")
    print(f"{RED}{BOLD}" + "=" * 76 + f"{RESET}\n")

def pause():
    input(f"\n{YELLOW}Press [Enter] to return to the investigation menu...{RESET}")

def view_vizag_map():
    print_header()
    print(f"{BOLD}=== 🗺️ VISAKHAPATNAM (VIZAG) & GITAM CAMPUS MAP ==={RESET}\n")
    print(f"  [1] {RED}★ GITAM University Campus, Rushikonda{RESET} (The Crime Scene)")
    print("      Executive Suite 501, Innovation Tower overlooking the beach road.")
    print(f"  [2] {YELLOW}Anandapuram Highway Toll Plaza (NH-16 Bypass){RESET}")
    print("      Highway loop connecting GITAM/Bheemili road to the national highway.")
    print(f"  [3] {GREEN}MVP Colony 24/7 Apollo Pharmacy{RESET}")
    print("      Where Kavya bought migraine medicine at 10:56 PM (12 min drive from GITAM).")
    print(f"  [4] {CYAN}Siripuram & Waltair Uplands{RESET}")
    print("      Inland neighborhood where Arjun claimed he was sitting on his balcony.")
    print(f"  [5] {WHITE}RK Beach & Submarine Museum{RESET}")
    print("      Vizag's ocean promenade, completely empty during the storm.")
    print(f"  [6] {PINK}Dolphin's Nose Lighthouse / Vizag Port{RESET}")
    print("      Marine foghorn audible only along the coastal belt (including GITAM)!")
    print("\nAll locations are within Greater Visakhapatnam!")
    pause()

def day1_briefing():
    print_header()
    print(f"{BOLD}=== 🗓️ DAY 1: GITAM UNIVERSITY CRIME SCENE INCIDENT REPORT ==={RESET}\n")
    print(f"{CYAN}[POLICE REPORT]:{RESET} 'First responders secured from the GITAM University campus.")
    print("Raghavendra Varma, CMD of Varma BioTech and Chief Patron of GITAM,")
    print("was found dead in his top-floor executive suite overlooking Rushikonda Beach.'\n")
    print(f"{PINK}[INCIDENT LOG]:{RESET} 'Raghavendra Varma found dead inside GITAM University.")
    print("tell me in plain English: what did your team find in his office?'\n")
    print(f"{BOLD}FIR #VIZ-309 DETAILS:{RESET}")
    print("  • Victim: Raghavendra 'Raghav' Varma (Age 56), slumped over his teakwood desk.")
    print("  • Location: Executive Suite 501, Innovation Tower, GITAM University, Rushikonda.")
    print("  • Found by: Assistant Kavya Reddy at 11:45 PM.")
    print("  • The Scene: Spilled copper mug of Kashmiri Kahwa tea on the Persian rug.")
    print("  • The Doors: Ocean-view glass sliding doors unlatched and left 4 inches open to storm.")
    print("  • The Safe: Wall safe behind the ship painting unlocked using PIN #808; patent deeds stolen.")
    print(f"\n{BOLD}THE 4 SUSPECTS ON GITAM CAMPUS:{RESET}")
    print("  1. Sree Nidhi Varma (49) - Wife (staying at GITAM VIP Guest House; ₹120 Cr property dispute).")
    print("  2. Dr. Ram Prasad (53) - Dean of Clinical Research at GIMSR (accused of embezzling ₹18.4 Cr).")
    print("  3. Arjun Rao (37) - Chief Technical Lead at GITAM Biotech Lab (furious about patent sale).")
    print("  4. Kavya Reddy (28) - Assistant who served tea water and drove to MVP Colony pharmacy.")
    pause()

def day2_forensics():
    print_header()
    print(f"{BOLD}=== 🗓️ DAY 2: KGH AUTOPSY & ANANDAPURAM TOLL LOGS ==={RESET}\n")
    print(f"{CYAN}[CORONER REPORT]:{RESET} 'King George Hospital (KGH) Vizag confirmed aconitine poison.")
    print("It takes exactly 25 to 35 minutes to cause cardiac arrest after drinking.'\n")
    print(f"{PINK}[KEY DEDUCTION]:{RESET} 'If Raghav died at 10:50 PM, the poison had to be swallowed")
    print("between 10:15 PM and 10:25 PM! That's when Dr. Ram was alone with him in his GITAM office!'\n")
    print(f"{BOLD}FASTag TOLL & GITAM GATE TIMELINE:{RESET}")
    logs = [
        ("10:05 PM", "GITAM Suite 501", "Kavya brings hot water kettle and tea spice box. Exits at 10:08 PM."),
        ("10:15 PM", "GITAM Suite 501", "Dr. Ram enters Raghav's office. Angry argument about audit papers."),
        ("10:26 PM", "GITAM Suite 501", "Dr. Ram leaves office, carrying his leather bag."),
        ("10:29 PM", "GITAM Main Gate", "Dr. Ram drives his White Fortuner out toward Bheemili."),
        ("10:36 PM", "GITAM Main Gate", "Kavya leaves for MVP Colony Apollo Pharmacy."),
        ("10:46 PM", "Anandapuram Toll", "[ANOMALY] Dr. Ram's FASTag triggers U-turn loop, speeding back toward GITAM!"),
        ("10:50 PM", "GITAM Suite 501", "Safe opened with PIN #808. Patent binder taken."),
        ("10:56 PM", "MVP Colony Apollo", "Kavya pays for migraine medicine (receipt verified)."),
        ("11:14 PM", "GITAM Beach Fence", "Man in dark coat spotted slipping through rear beach fence on foot."),
        ("11:42 PM", "GITAM Main Gate", "Kavya returns; discovers body at 11:45 PM.")
    ]
    for ts, loc, desc in logs:
        print(f"  {YELLOW}{ts}{RESET} | {CYAN}{loc:<20}{RESET} | {desc}")
    pause()

def day3_hidden_clues():
    print_header()
    print(f"{BOLD}=== 🗓️ DAY 3: FIVE CRITICAL HIDDEN CLUES ==={RESET}\n")
    print(f"{YELLOW}[CLUE A] Araku Wild Forest Honey Jar & Dropper:{RESET}")
    print("  Raghav sweetened his tea with Araku forest honey. Chemical testing showed aconitine")
    print("  mixed with lavender oil to hide the bitterness. A doctor's dropper was in the wastebasket.")
    print(f"\n{YELLOW}[CLUE B] The 10:42 PM Audio & Dolphin's Nose Foghorn:{RESET}")
    print("  Arjun sent a voice note at 10:42 PM claiming he was in Siripuram. In the background,")
    print("  the coastal foghorn of the Dolphin's Nose Lighthouse is clearly audible! Siripuram is 6 km")
    print("  inland behind hills—Arjun was parked right near GITAM Beach!")
    print(f"\n{YELLOW}[CLUE C] Safe Sign-Out Log & Left-Handed Smudge:{RESET}")
    print("  The register inside the safe has a signature at 10:50 PM smudged to the right by a LEFT hand.")
    print("  Dr. Ram, Sree Nidhi, and Kavya are right-handed. Only Arjun Rao is LEFT-HANDED!")
    print(f"\n{YELLOW}[CLUE D] Sree Nidhi's Apple Watch Telemetry:{RESET}")
    print("  Her watch logged 280 steps and her pulse jumped to 142 BPM at 10:58 PM. She admits she ran")
    print("  across the campus garden in the rain and saw Arjun inside the office with Raghav's body!")
    print(f"\n{YELLOW}[CLUE E] Shredded Complaint to Vizag Police Commissioner:{RESET}")
    print("  'Formal complaint against Dr. Ram Prasad for embezzling ₹18.4 Crores from GIMSR. Monday 10 AM.'")
    pause()

def day4_interrogation():
    while True:
        print_header()
        print(f"{BOLD}=== 🗓️ DAY 4: INTERROGATION ROOM AT VIZAG CCS ==={RESET}\n")
        print("Select suspect statement to review:")
        print("  1. Dr. Ram Prasad (Dean of Research, GIMSR)")
        print("  2. Sree Nidhi Varma (Wife & Trustee)")
        print("  3. Arjun Rao (Biotech Lab Technical Lead)")
        print("  4. Kavya Reddy (Executive Assistant)")
        print("  0. Back to Main Menu")

        ch = input(f"\n{YELLOW}Select suspect (0-4): {RESET}").strip()
        if ch == '0':
            break
        elif ch == '1':
            print(f"\n{BOLD}Cross-examining Dr. Ram Prasad:{RESET}")
            print(f"{CYAN}Investigator: 'Why did your FASTag show a U-turn at Anandapuram Toll at 10:46 PM?'{RESET}")
            print("Dr. Ram: 'Raghav threatened to turn my ₹18.4 Cr embezzlement over to the Vizag police.")
            print("After leaving GITAM at 10:29 PM, I had a panic attack at Anandapuram Toll. I realized his audit")
            print("ledger was on his desk. I took the U-turn to sneak through the rear beach fence and steal")
            print("the folder back! But by the time I reached the beach fence at 11:14 PM, Kavya was screaming. I ran!'")
            pause()
        elif ch == '2':
            print(f"\n{BOLD}Cross-examining Sree Nidhi Varma:{RESET}")
            print(f"{PINK}Investigator: 'Your Apple Watch shows your heart rate jumped to 142 BPM at 10:58 PM.'{RESET}")
            print("Sree Nidhi: 'I heard noises at 10:50 PM. I walked across the campus garden in the rain and looked through the")
            print("glass sliding door at 11:00 PM. Raghav was already collapsed on his desk! And Arjun Rao was standing")
            print("over the safe stuffing patent files into his bag! I ran back terrified Arjun would kill me!'")
            pause()
        elif ch == '3':
            print(f"\n{BOLD}Cross-examining Arjun Rao:{RESET}")
            print(f"{CYAN}Investigator: 'The Dolphin's Nose coastal foghorn proves you were at GITAM Beach at 10:42 PM.'{RESET}")
            print("Arjun: 'Fine! I came to take back my patent before Raghav sold it. I used Kavya's safe code.")
            print("When I entered Suite 501 at 10:50 PM, RAGHAV WAS ALREADY DEAD! His face was blue, and his tea")
            print("was spilled. I checked his carotid pulse—he was gone! I took my patent, signed the log with")
            print("my left hand, and fled! Whoever poisoned him did it before 10:30 PM!'")
            pause()
        elif ch == '4':
            print(f"\n{BOLD}Cross-examining Kavya Reddy:{RESET}")
            print(f"{PINK}Investigator: 'Did Raghav drink his tea when you served it at 10:05 PM?'{RESET}")
            print("Kavya: 'No! The water was still steeping. Raghav said he would drink it during his 10:15 PM")
            print("consultation with Dr. Ram. Raghav always used his personal Araku forest honey jar on the desk credenza.'")
            pause()

def file_chargesheet():
    print_header()
    print(f"{RED}{BOLD}=== ⚖️ FINAL CHARGESHEET SUBMISSION (FORM 42-A) ==={RESET}\n")

    print(f"{BOLD}1. Who is the murderer?{RESET}")
    print("   [1] Sree Nidhi Varma")
    print("   [2] Dr. Ram Prasad")
    print("   [3] Arjun Rao")
    print("   [4] Kavya Reddy")
    ans1 = input(f"{YELLOW}Choice (1-4): {RESET}").strip()

    print(f"\n{BOLD}2. How was the poison administered?{RESET}")
    print("   [1] Electric kettle in pantry at 9:55 PM.")
    print("   [2] Spiked Araku wild honey jar on the desk with aconitine masked in lavender oil during 10:15 PM-10:25 PM in GITAM Suite 501.")
    print("   [3] Aerosolized gas pumped through terrace at 11:00 PM.")
    ans2 = input(f"{YELLOW}Choice (1-3): {RESET}").strip()

    print(f"\n{BOLD}3. Ingestion timeline matching the 25-35 minute lethal curve?{RESET}")
    print("   [1] Swallowed at 10:20 PM-10:25 PM; fatal collapse occurred at 10:50 PM-10:55 PM.")
    print("   [2] Swallowed at 10:05 PM; fatal collapse occurred at 10:30 PM.")
    print("   [3] Swallowed at 11:30 PM right before Kavya returned.")
    ans3 = input(f"{YELLOW}Choice (1-3): {RESET}").strip()

    print(f"\n{BOLD}4. What breaks the killer's alibi?{RESET}")
    print("   [1] FASTag toll loop at Anandapuram proving Dr. Ram returned to sneak into GITAM.")
    print("   [2] Arjun's foghorn proving he poisoned the tea.")
    print("   [3] Sree Nidhi's Apple Watch telemetry.")
    ans4 = input(f"{YELLOW}Choice (1-3): {RESET}").strip()

    print(f"\n{BOLD}5. Explanation of secondary crimes (red herrings)?{RESET}")
    print("   [1] All 4 planned a joint murder.")
    print("   [2] Independent acts: Arjun (left-handed) stole the patent binder at 10:50 PM after Raghav was already dead; Sree Nidhi spied from the lawn; Dr. Ram was the sole poisoner.")
    print("   [3] Kavya masterminded the killing.")
    ans5 = input(f"{YELLOW}Choice (1-3): {RESET}").strip()

    is_correct = (ans1 == '2' and ans2 == '2' and ans3 == '1' and ans4 == '1' and ans5 == '2')

    print("\n" + "=" * 60)
    print(f"{YELLOW}SUBMITTING TO VIZAG PUBLIC PROSECUTOR...{RESET}")
    time.sleep(1)

    if is_correct:
        print(f"\n{GREEN}{BOLD}🎉 CHARGESHEET ACCEPTED! 100% CONVICTION SECURED!{RESET}\n")
        print(f"{GREEN}[VERDICT]:{RESET} 'Case closed! All evidence is airtight: Every deduction was airtight:'")
        print("1. Dr. Ram Prasad faced ruin for embezzling ₹18.4 Crores from GIMSR.")
        print("2. Spiked Raghav's Araku wild honey jar with aconitine masked in lavender oil during the 10:15 PM-10:25 PM argument.")
        print("3. Swallowed at ~10:25 PM, fatal cardiac collapse occurred at ~10:50 PM.")
        print("4. Dr. Ram's FASTag U-turn at Anandapuram Toll broke his alibi completely.")
        print("5. Arjun stole the patent with his left hand after Raghav died; Sree Nidhi spied from the lawn.")
        print(f"\n{GREEN}{BOLD}CASE CLOSED // DR. RAM PRASAD INDICTED FOR FIRST-DEGREE MURDER!{RESET}")
    else:
        print(f"\n{RED}{BOLD}❌ CHARGESHEET REJECTED BY PUBLIC PROSECUTOR!{RESET}\n")
        print(f"{RED}[DISTRICT ATTORNEY]:{RESET} 'Warrant rejected! Check your notes again: There is an inconsistency in our logic.'")
    pause()

def main():
    while True:
        print_header()
        print(f"{BOLD}GITAM UNIVERSITY HOMICIDE INVESTIGATION MENU:{RESET}")
        print("  [1] 🗺️ View Visakhapatnam (Vizag) & GITAM Campus Map")
        print("  [2] 🗓️ Day 1: Crime Scene Incident Report (GITAM Suite 501)")
        print("  [3] 🗓️ Day 2: KGH Autopsy & Anandapuram Toll Logs")
        print("  [4] 🗓️ Day 3: The 5 Hidden Clues (Dolphin's Nose Foghorn, Honey Jar)")
        print("  [5] 🗓️ Day 4: Interrogation Room at Vizag CCS")
        print("  [6] ⚖️ Submit Final Chargesheet to Prosecutor")
        print("  [0] Close Dossier")

        ch = input(f"\n{YELLOW}Select file (0-6): {RESET}").strip()
        if ch == '1':
            view_vizag_map()
        elif ch == '2':
            day1_briefing()
        elif ch == '3':
            day2_forensics()
        elif ch == '4':
            day3_hidden_clues()
        elif ch == '5':
            day4_interrogation()
        elif ch == '6':
            file_chargesheet()
        elif ch == '0':
            print(f"\n{CYAN}Closing Vizag case files. Good work, Detective!{RESET}\n")
            sys.exit(0)
        else:
            print(f"{RED}Invalid input. Enter 0-6.{RESET}")
            time.sleep(0.5)

if __name__ == '__main__':
    main()
