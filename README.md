# Aproximal numerical system paradigm
## OpenSesame experiment adaptation
**Authors:**<br>

- Michala Plassova
- Michal Vavrecka
- Michael Tesar

**Web:**
[http://www.pf.jcu.cz/structure/departments/kpe/neurolab/](http://www.pf.jcu.cz/structure/departments/kpe/neurolab/)

**Version:**
```
pilot stage
```
2nd pilot measurement is planned to 30.9.2016

**Quick notes:**
- We should include a block pause (5 block in the row, then manual pause with 8 times repetition)
- Run lasted about 20 minutes (14 blocks) 

## How to download
First download Github desktop app or any other Git client if needed. Then download repository by git command or in any Git application by user graphical interface.

Download GitHub desktop app [here](https://desktop.github.com).
```
git clone https://github.com/neurolab-ju/ans-os.git
```

## How to run
You need to install OpenSesame on your operating system. Paradigm is written on macOS Sierra but is completly cross-platform so you can run experiment on Windows, Linux and maxOS.
 1. Download and install OpenSesame 3.1 at [http://osdoc.cogsci.nl/3.1/download/](http://osdoc.cogsci.nl/3.1/download/)
 1. Download latest version of experiment here on GitHub or by you Git client
 1. Open downloaded experiment in OpenSesame (*.osexp)
 1. Run experiment with ctrl + R (Windows, probably Linux) or ⌘ + R (macOS)

# Paradigm scheme
| Screen name  | Description                             | Type      | Duration | Log              | Name        |
|--------------|-----------------------------------------|-----------|----------|------------------|-------------|
| Fish cluster | Main experimental stimuli               | Sketchpad | 1500 ms  | Onset            | FishCluster |
| Blank answer | Blank black screen with + with response | Sketchpad | infinite | RT + FishCluster | BlankAnswer |

This is done in loop cycle for difficulty logs from 2.5 (LOG_25)to 1.1 (LOG_11). But event that it is specified in inicialization script handy variables such as:

```python
MAX_LOG = 25    # maximum log difficulty of 2.5
MIN_LOG = 11    # minimum log difficulty of 1.1
DEBUG = True    # set debugging setter to "yes"
LEVEL = 24      # experiment start at log difficulty of 2.4
STIMULI_DURATION = 1500 # duration of FishCluster sketchpad
BLOCK_COUNTER = 6 # declare and initialize maximum block appearence
BLOCK_CYCLES = 5  # declare and initialize block counter in one cycle
```

Each round is specified of its **log difficulty** setted up by number from 25 (log 2.5 - super easy) to 11 (log 1.1 pretty hard). This one round starts at log difficulty 2.4 (LOG_24) and contains (same as other rounds) **10 trials per round**. Each of those trials are counter ballanced (there is equal chance to orange and blue fish appearence). After round ends experiment computes its score based on main loop cycle. If participant **score < 6 = level down, score > 6 = level up** or **score = 6** keep level. This is because when there is counter-ballance condition and participant would keeps pressing one button, then it would pass to next level or keep the particular level. If he do this we expect him to not know the correct answers and should go level down, e.g. easier version of fish cluster.

Five rounds represents **one block** which takes about 4 minutes. Then goes manully continuous (keypress on keyboard) pause. After that goes another block and another one until 6 times which takes about 24 minutes of plain experiment.

# Technical informations
## EEG triggers
| Log difficulty | Trigger in EEG |
|----------------|----------------|
| 2.5            | 25             |
| 2.4            | 24             |
| 2.3            | 23             |
| 2.2            | 22             |
| 2.1            | 21             |
| 2.0            | 20             |
| 1.9            | 19             |
| 1.8            | 18             |
| 1.7            | 17             |
| 1.6            | 16             |
| 1.5            | 15             |
| 1.4            | 14             |
| 1.3            | 13             |
| 1.2            | 12             |
| 1.1            | 11             |

### Another EEG triggers
| Event            | Trigger in EEG |
| EEG start        | 254            |
| EEG stop         | 255            |
| Correct answer   | 1              |
| Incorrect answer | 2              |

EEG start after main instructions (in 3, 2, 1...go) and end after main loop finish (before ending instructions).

# Advanced
## Another software
- Stimuli generator [https://github.com/Neurolab-JU/ans-generator](https://github.com/Neurolab-JU/ans-generator) - MATLAB
- Fibonacci grid calculator [https://github.com/Neurolab-JU/fibonacci-disk-grid](https://github.com/Neurolab-JU/fibonacci-disk-grid) - MATLAB
- Original version in presentation [https://github.com/Neurolab-JU/ans-generator](https://github.com/Neurolab-JU/ans-generator)

## Response collection
Response is done by gaming mouse with smalles possible latency (wired) which has orange and blue label on it represents buttons to press as answer on main experimental task.
- Orange - LMB
- Blue - RMB

## Newer versions possible modifications
- [ ] Answers are picked in blank gap called BlankAnswer
- [ ] Contains custom log file
- [ ] After experiment finish there is overview screen (sketchpad)
- [ ] New instuction stimuli (start in 3..2..1...go, this is testing you can try this out, this is pause do what you want)

# Additional recommendations
 1. Prepare and send me new instructions
 2. Think about SB task in tablet (it takes some time to code it and test it - several weeks)
 3. Test final experiment (behavioral) before 2nd pilot
 4. Define training (Zácvik) - whichi stimuli and instruction and form


