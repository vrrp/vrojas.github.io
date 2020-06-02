---
title: ":Covid-19: Sudamerica"
layout: post
date: 2020-03-06 17:00
tag: csharp
image: https://roseleblood.github.io/openess/Logo-OpenESS.png
headerImage: false
projects: true
hidden: true # don't count this post in blog pagination
description: "virtual Chip with own instruction set and IDE with Compiler and Debugger"
category: project
author: roseleblood
externalLink: false
---

---

# virtualSoC
virtual Chip with own instruction set and IDE with Compiler and Debugger (viSoC Studio 2018)

## viSoC Studio 2018
IDE for the virtual Chip

Demo PreRelease https://github.com/RoseLeBlood/virtualSoC/releases

![Screenshot]( https://raw.githubusercontent.com/RoseLeBlood/virtualSoC/master/images/viSoCStudio2018.png)


## Current using Mnemonic
* NOP: No operating - NOP
* HLT: Beendet das Programm - HLT
* ADD: Add Number, Register, Pointer to AX - ADD #d5
* CLR: Setze pointer oder register auf 0 - CLR AX
* DIV: Div Number, Register, Pointer to AX - DIV #d5
* JMP: Jump zu Adresse - JMP Test
* MUL: Mul Number, Register, Pointer to AX - MUL #d5
* PEEK: Lese aktullen Wert auf den Stack  - PEEK @d255
* POP: Pop element vom Stack - POP @d255
* PUSH: Puscht element auf den Stack - PUSH @d255
* SUB: Sub Number, Register, Pointer to AX - SUB #d5
* MOV: Setze Pointer oder Register Wert   - MOV AX, #d5
* OR: Oder Operator2 Operator3 to Operator1 - OR @d255, #d5, #d5
* XOR: Exclusiv Oder Operator2 Operator3 to Operator1 - XOR @d255, #d5, #d5
* AND: And Operator2 Operator3 to Operator1 AND @d255, #d5, #d5
* NOR: Nicht oder Operator2 Operator3 to Operator1 - NOR @d255, #d5, #d5
* NXOR: Nicht exclusiv oder Operator2 Operator3 to Operator1 - NXOR @d255, #d5, #d5
* NOT: NOT Operator2 to Operator1 NOT @d255, #d5
* NAND: Not And Operator2 Operator3 to Operator1 - NAND @d255, #d5, #d5
* CALL: Springe zum unter Programm und lege ip+9 in den stack
* RET: Springe zurück aus dem Unterprogramm - RET
* FBI: Initalisiert den Framebuffer - FBI
* FBSET: Setzt ein Pixel an position x, y - FBSET #d5, #d5, #hff0000
* ADR: Add Operator2 Operator3 to Operator1 ADR @d255, #d5, #d5
* SBR: Sub Operator2 Operator3 to Operator1 - SBR @d255, #d5, #d5
* DVR: Div Operator2 Operator3 to Operator1 DVR @d255, #d5, #d5
* MLR: Multiplikation Operator2 Operator3 to Operator1 MLR @d255, #d5, #d5
* JO: Jump wenn OverFlow Flag 1 ist - JO test
* JC: Jump wenn Carry 1 ist - JC @d255
* JNC: Jump wenn Carry 0 ist JNC Test
* JN0: Jump wenn OverFlow Flag 0 ist - JNO test
* INC: Incremiert ein Pointer oder Register - INC @d255
* DEC: Decriment Pointer oder Register - DEC AX
* STO: Setze pointer oder register auf 1 - STO AX
* INV: Invetiere ein Pointer oder Register - Inv @d255
