#!/usr/bin/env python3
"""
VISAKHAPATNAM POLICE DEPT // CENTRAL CRIME STATION
INTERACTIVE PEN & PAPER HOMICIDE MYSTERY ARCHIVE
Case #1: The GITAM University Murder (Rushikonda Beach)
Case #2: The Araku Vistadome Enigma (The Ghost in Tunnel 22)
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

def pause():
    input(f"\n{YELLOW}Press [Enter] to return to the investigation menu...{RESET}")

# ========================================================
# CASE 1: THE GITAM UNIVERSITY MURDER
# ========================================================
def run_case_1():
    while True:
        print(f"\n{RED}{BOLD}" + "=" * 76 + f"{RESET}")
        print(f"{RED}{BOLD}  CASE #VIZ-309: THE GITAM UNIVERSITY MURDER (RUSHIKONDA CAMPUS){RESET}")
        print(f"{CYAN}  VICTIM: Raghavendra 'Raghav' Varma (Age 56) | CMD, Varma BioTech{RESET}")
        print(f"{RED}{BOLD}" + "=" * 76 + f"{RESET}\n")

        print(f"{BOLD}INVESTIGATION MENU:{RESET}")
        print("  [1] 🗺️ View Visakhapatnam & GITAM Campus Map")
        print("  [2] 🗓️ Day 1: Crime Scene Incident Report (Suite 501)")
        print("  [3] 🗓️ Day 2: KGH Autopsy & Anandapuram Toll Timeline")
        print("  [4] 🗓️ Day 3: Five Critical Hidden Clues")
        print("  [5] 🎙️ Day 4: Interrogation Room at Vizag CCS")
        print("  [6] ⚖️ Submit Final Court Chargesheet (Form 42-A)")
        print("  [0] Return to Master Case Selector")

        ch = input(f"\n{YELLOW}Select option (0-6): {RESET}").strip()
        if ch == '0':
            break
        elif ch == '1':
            print(f"\n{BOLD}=== 🗺️ VIZAG & GITAM MAP LOCATIONS ==={RESET}")
            print(f"  ★ 1. {RED}GITAM University Campus, Rushikonda{RESET} - Executive Suite 501.")
            print(f"  2. {YELLOW}Anandapuram Highway Toll Plaza{RESET} - Where Dr. Ram's car looped at 10:46 PM.")
            print(f"  3. {GREEN}MVP Colony 24/7 Apollo Pharmacy{RESET} - Kavya's medicine errand at 10:56 PM.")
            print(f"  4. {CYAN}Siripuram & Waltair Uplands{RESET} - Arjun's claimed alibi location.")
            print(f"  5. {WHITE}RK Beach Promenade{RESET} - Stormy coastal road.")
            print(f"  6. {PINK}Dolphin's Nose Lighthouse / Vizag Port{RESET} - Foghorn source audible at GITAM.")
            pause()
        elif ch == '2':
            print(f"\n{BOLD}=== 🗓️ DAY 1: GITAM UNIVERSITY INCIDENT REPORT ==={RESET}")
            print("  • Victim: Raghavendra Varma, found slumped across his desk at 11:45 PM.")
            print("  • Scene: Spilled copper mug of Kashmiri Kahwa tea; ocean balcony unlatched.")
            print("  • Safe: Opened using PIN #808; patent deeds stolen.")
            print("  • Suspects: Sree Nidhi (Wife), Dr. Ram (Dean of Research), Arjun (Lab Lead), Kavya (Assistant).")
            pause()
        elif ch == '3':
            print(f"\n{BOLD}=== 🗓️ DAY 2: KGH AUTOPSY & FASTAG TIMELINES ==={RESET}")
            print("  • KGH Autopsy: Fatal aconitine poisoning; cardiac arrest takes 25-35 minutes.")
            print("  • Ingestion Window: 10:15 PM - 10:25 PM (when Dr. Ram was alone in the room).")
            print("  • FASTag Anomaly: Dr. Ram drove out at 10:29 PM, made a U-turn at Anandapuram Toll at 10:46 PM,")
            print("    and snuck back into GITAM on foot through the rear beach fence at 11:14 PM!")
            pause()
        elif ch == '4':
            print(f"\n{BOLD}=== 🗓️ DAY 3: FIVE CRITICAL HIDDEN CLUES ==={RESET}")
            print("  [CLUE A] Araku honey jar spiked with lavender-scented aconitine; dropper in trash.")
            print("  [CLUE B] Dolphin's Nose foghorn audible in Arjun's voice note (proves he was at GITAM, not Siripuram).")
            print("  [CLUE C] Safe log signature smudged to the right by a LEFT hand (only Arjun is left-handed).")
            print("  [CLUE D] Sree Nidhi's Apple Watch spiked to 142 BPM at 10:58 PM when she saw Arjun in the office.")
            print("  [CLUE E] Shredded draft complaint to Police Commissioner regarding Dr. Ram's ₹18.4 Cr embezzlement.")
            pause()
        elif ch == '5':
            print(f"\n{BOLD}=== 🎙️ DAY 4: INTERROGATION ROOM ==={RESET}")
            print("  • Dr. Ram confessed to making the U-turn to sneak back and steal the audit ledger.")
            print("  • Arjun confessed to stealing the patent, but swore Raghav was already dead at 10:50 PM.")
            print("  • Sree Nidhi admitted she spied from the garden and saw Arjun with the dead body.")
            print("  • Kavya confirmed Raghav only sweetened his tea during Dr. Ram's 10:15 PM consultation.")
            pause()
        elif ch == '6':
            print(f"\n{BOLD}=== ⚖️ SUBMIT CHARGESHEET (CASE 1) ==={RESET}")
            ans1 = input("1. Primary Murder Accused (1: Sree Nidhi, 2: Dr. Ram, 3: Arjun, 4: Kavya): ").strip()
            ans2 = input("2. Method (1: Kettle, 2: Araku honey jar with lavender-masked aconitine, 3: Gas): ").strip()
            ans3 = input("3. Ingestion Window (1: 10:20-10:25 PM, 2: 10:05 PM, 3: 11:30 PM): ").strip()
            ans4 = input("4. Breaking Proof (1: FASTag U-turn at Anandapuram Toll, 2: Foghorn, 3: Watch): ").strip()
            ans5 = input("5. Secondary Crimes (1: Conspiracy, 2: Independent opportunistic acts): ").strip()

            if ans1 == '2' and ans2 == '2' and ans3 == '1' and ans4 == '1' and ans5 == '2':
                print(f"\n{GREEN}{BOLD}🎉 100% CONVICTION SECURED! DR. RAM PRASAD INDICTED FOR MURDER!{RESET}")
            else:
                print(f"\n{RED}{BOLD}❌ CHARGESHEET REJECTED! Review the evidence logs and try again.{RESET}")
            pause()

# ========================================================
# CASE 2: THE ARAKU VISTADOME ENIGMA (TUNNEL 22)
# ========================================================
def run_case_2():
    while True:
        print(f"\n{GREEN}{BOLD}" + "=" * 76 + f"{RESET}")
        print(f"{GREEN}{BOLD}  CASE #VIZ-410: THE ARAKU VISTADOME ENIGMA (THE GHOST IN TUNNEL 22){RESET}")
        print(f"{CYAN}  VICTIM: Bhadri Raju (Age 62) | Coffee Tycoon | SCENE: Coach EV-1{RESET}")
        print(f"{GREEN}{BOLD}" + "=" * 76 + f"{RESET}\n")

        print(f"{BOLD}INVESTIGATION MENU:{RESET}")
        print("  [1] 🚂 View Vistadome Coach EV-1 Seating & Tunnel Route")
        print("  [2] 📋 Incident Report (The 3m 40s Blackout & Locked Coach)")
        print("  [3] ⏱️ Tunnel 22 Running Timeline (8:42:00 AM - 8:45:40 AM)")
        print("  [4] 🔎 Five Critical Forensic Clues (Dagger Angle & Moss)")
        print("  [5] 🎙️ Passenger Interrogations at Borra Caves Station")
        print("  [6] ⚖️ Submit Indictment to Railway Magistrate (Form 108)")
        print("  [0] Return to Master Case Selector")

        ch = input(f"\n{YELLOW}Select option (0-6): {RESET}").strip()
        if ch == '0':
            break
        elif ch == '1':
            print(f"\n{BOLD}=== 🚂 COACH EV-1 SEATING LAYOUT ==={RESET}")
            print(f"  • {RED}Seat 14 (VICTIM): Bhadri Raju{RESET} - Swiveled 90° facing window; 14-inch gap.")
            print(f"  • {CYAN}Seat 13: Meera Sen{RESET} - Private secretary carrying briefcase code #914.")
            print(f"  • {YELLOW}Seat 12: Vikram Varma{RESET} - Nephew across aisle; 6'2\", 95 kg (in heavy debt).")
            print(f"  • {GREEN}Seat 15: Dr. Lavanya Chari{RESET} - Environmental activist seated directly behind.")
            print(f"  • {MAGENTA}Seat 8: Kishore Naidu{RESET} - Coffee consortium director in front row.")
            print(f"  • {WHITE}Rear Cubicle: TTE Surya Prakash{RESET} - Locked both vestibule doors at 8:40 AM.")
            print(f"  • {BLUE}Rear Lounge Water Dispenser{RESET} - Chilled ice reservoir.")
            pause()
        elif ch == '2':
            print(f"\n{BOLD}=== 📋 INCIDENT REPORT: TUNNEL 22 (KM 84/6) ==={RESET}")
            print("  • Train 18551 Vistadome entered Tunnel 22 (2,750 m) at 8:42:00 AM.")
            print("  • Generator breaker tripped; coach EV-1 was in pitch darkness for 3m 40s.")
            print("  • Both end doors were locked from the inside by the TTE.")
            print("  • Train emerged onto Galikonda bridge at 8:45:40 AM; Bhadri Raju found stabbed to death.")
            print("  • The 120-carat Kalinga Emerald was stolen from his titanium briefcase.")
            pause()
        elif ch == '3':
            print(f"\n{BOLD}=== ⏱️ TUNNEL 22 MASTER TIMELINE ==={RESET}")
            print("  8:40:00 AM - TTE Surya Prakash locks both vestibule doors.")
            print("  8:42:00 AM - Train enters Tunnel 22. Breaker trips. Pitch darkness begins.")
            print("  8:43:15 AM - Soft scuffle heard near Seat 13/14 over rail roar.")
            print("  8:44:20 AM - Kishore Naidu shouts: 'Someone brushed past my shoulder in the dark!'")
            print("  8:45:40 AM - Train exits Tunnel 22 into bright sunlight on bridge. Body discovered!")
            pause()
        elif ch == '4':
            print(f"\n{BOLD}=== 🔎 FIVE CRITICAL FORENSIC CLUES ==={RESET}")
            print("  [CLUE 1] Dagger Angle: Thrust upward from narrow 14-inch window gap. A 95kg man cannot fit!")
            print("  [CLUE 2] Cave Moss: Rare tunnel wall moss (*Dictyostelium*) found on Meera Sen's shawl hem.")
            print("  [CLUE 3] Secret Audio: Dr. Lavanya's recorder caught a female voice counting strides in Telugu.")
            print("  [CLUE 4] Stolen Emerald: 120-carat emerald found inside ice flask in lounge dispenser with Meera's print.")
            print("  [CLUE 5] Breaker Tampering: The lighting breaker was wedged open with a coffee stirrer having red lipstick.")
            pause()
        elif ch == '5':
            print(f"\n{BOLD}=== 🎙️ PASSENGER INTERROGATIONS ==={RESET}")
            print("  • Vikram: Confessed he fumbled in the dark to steal his forged will, but found Bhadri already dead.")
            print("  • Dr. Lavanya: Her recorder caught ambient sound including the counting footsteps.")
            print("  • Kishore: Confirmed someone tall (Vikram) brushed past him in the aisle.")
            print("  • Meera: Froze when confronted with her lipstick on the stirrer and prints on the thermos!")
            pause()
        elif ch == '6':
            print(f"\n{BOLD}=== ⚖️ SUBMIT INDICTMENT (CASE 2) ==={RESET}")
            ans1 = input("1. Primary Murder Accused (1: Vikram, 2: Dr. Lavanya, 3: Kishore, 4: Meera Sen, 5: TTE): ").strip()
            ans2 = input("2. Method (1: Breaker stealth & window gap thrust, 2: Thrown dagger, 3: Poison): ").strip()
            ans3 = input("3. Breaking Proof (1: Meera's prints on submerged thermos & lipstick on stirrer, 2: Debts): ").strip()
            ans4 = input("4. Secondary Acts (1: Vikram fumbled for will; Dr. Lavanya recorded; independent, 2: Conspiracy): ").strip()

            if ans1 == '4' and ans2 == '1' and ans3 == '1' and ans4 == '1':
                print(f"\n{GREEN}{BOLD}🎉 CASE SOLVED! MEERA SEN CONVICTED OF FIRST-DEGREE MURDER & THEFT!{RESET}")
                print("She planned the heist, wedged the breaker, counted strides, and stashed the emerald in the ice dispenser!")
            else:
                print(f"\n{RED}{BOLD}❌ INDICTMENT REJECTED BY RAILWAY MAGISTRATE! Review clues and retry.{RESET}")
            pause()

def main():
    while True:
        print(f"\n{BOLD}========================================================================{RESET}")
        print(f"{BOLD}  VISAKHAPATNAM POLICE // CENTRAL CRIME STATION // CASE SELECTOR{RESET}")
        print(f"{BOLD}========================================================================{RESET}\n")
        print("Which case file would you like to investigate?")
        print(f"  [1] 📁 {RED}Case #VIZ-309: The GITAM University Murder{RESET} (Rushikonda Beach)")
        print(f"  [2] 🚂 {GREEN}Case #VIZ-410: The Araku Vistadome Enigma{RESET} (The Ghost in Tunnel 22)")
        print("  [0] Exit Case Archives")

        choice = input(f"\n{YELLOW}Select case (0-2): {RESET}").strip()
        if choice == '1':
            run_case_1()
        elif choice == '2':
            run_case_2()
        elif choice == '0':
            print(f"\n{CYAN}Closing detective files. Stay sharp!{RESET}\n")
            sys.exit(0)
        else:
            print(f"{RED}Invalid choice.{RESET}")
            time.sleep(0.5)

if __name__ == '__main__':
    main()
