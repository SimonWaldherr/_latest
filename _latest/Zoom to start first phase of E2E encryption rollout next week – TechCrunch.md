--- 
extends: _layouts.post 
section: content 
image: https://techcrunch.com/wp-content/uploads/2019/04/GettyImages-925049712.jpg?w=536 
title: > 
  Zoom to start first phase of E2E encryption rollout next week – TechCrunch 
description: > 
  Zoom will begin rolling out end-to-end encryption to users of its videoconferencing platform from next week, it said today.Next week’s roll out of a technical preview is phase 1 of a four-stage process to bring E2E encryption to the platform.All meeting participants must have the E2EE setting enabled in order to join an E2EE meeting.If you’re wondering how you can be sure you’ve joined an E2EE Zoom meeting a dark padlock will be displayed atop the green shield icon in the upper left corner of the meeting screen.Meeting participants will also see the meeting leader’s security code — which they can use to verify the connection is secure. 
date: 1602698696.35813 
--- 
Zoom will begin rolling out end-to-end encryption to users of its videoconferencing platform from next week, it said today.

The platform, whose fortunes have been supercharged by the pandemic-driven boom in remote working and socializing this year, has been working on rebooting its battered reputation in the areas of security and privacy since April — after it was called out on misleading marketing claims of having E2E encryption (when it did not). E2E is now finally on its way though.

“We’re excited to announce that starting next week, Zoom’s end-to-end encryption (E2EE) offering will be available as a technical preview, which means we’re proactively soliciting feedback from users for the first 30 days,” it writes in a blog post. “Zoom users — free and paid — around the world can host up to 200 participants in an E2EE meeting on Zoom, providing increased privacy and security for your Zoom sessions.”

Zoom acquired Keybase in May, saying then that it was aiming to develop “the most broadly used enterprise end-to-end encryption offering”.

However, initially, CEO Eric Yuan said this level of encryption would be reserved for fee-paying users only. But after facing a storm of criticism the company enacted a swift U-turn — saying in June that all users would be provided with the highest level of security, regardless of whether they are paying to use its service or not.

Zoom confirmed today that Free/Basics users who want to get access to E2EE will need to participate in a one-time verification process — in which it will ask them to provide additional pieces of information, such as verifying a phone number via text message — saying it’s implementing this to try to reduce “mass creation of abusive accounts”.

“We are confident that by implementing risk-based authentication, in combination with our current mix of tools — including our work with human rights and children’s safety organizations and our users’ ability to lock down a meeting, report abuse, and a myriad of other features made available as part of our security icon — we can continue to enhance the safety of our users,” it writes.

Next week’s roll out of a technical preview is phase 1 of a four-stage process to bring E2E encryption to the platform.

This means there are some limitations — including on the features that are available in E2EE Zoom meetings (you won’t have access to join before host, cloud recording, streaming, live transcription, Breakout Rooms, polling, 1:1 private chat, and meeting reactions); and on the clients that can be used to join meetings (for phase 1 all E2EE meeting participants must join from the Zoom desktop client, mobile app, or Zoom Rooms).

The next phase of the E2EE rollout — which will include “better identity management and E2EE SSO integration”, per Zoom’s blog — is “tentatively” slated for 2021.

From next week, customers wanting to check out the technical preview must enable E2EE meetings at the account level and opt-in to E2EE on a per-meeting basis.

All meeting participants must have the E2EE setting enabled in order to join an E2EE meeting. Hosts can enable the setting for E2EE at the account, group, and user level and can be locked at the account or group level, Zoom notes in an FAQ.

The AES 256-bit GCM encryption that’s being used is the same as Zoom currently uses but here combined with public key cryptography — which means the keys are generated locally, by the meeting host, before being distributed to participants, rather than Zoom’s cloud performing the key generating role.

“Zoom’s servers become oblivious relays and never see the encryption keys required to decrypt the meeting contents,” it explains of the E2EE implementation.

If you’re wondering how you can be sure you’ve joined an E2EE Zoom meeting a dark padlock will be displayed atop the green shield icon in the upper left corner of the meeting screen. (Zoom’s standard GCM encryption shows a checkmark here.)

Meeting participants will also see the meeting leader’s security code — which they can use to verify the connection is secure. “The host can read this code out loud, and all participants can check that their clients display the same code,” Zoom notes.