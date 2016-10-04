# Aproximal Numerical System Paradigm in Kids
Michala Plassová, Michal Vavrečka and Michael Tesař. 2016. University of South Bohemia.
[![DOI](https://zenodo.org/badge/68840528.svg)](https://zenodo.org/badge/latestdoi/68840528)

**Web:**
[http://www.pf.jcu.cz/structure/departments/kpe/neurolab/](http://www.pf.jcu.cz/structure/departments/kpe/neurolab/)

**Version:**
```
1.2b
```

## How to run
You need to install OpenSesame on your operating system. Paradigm is written on macOS Sierra but is completly cross-platform so you can run experiment on Windows, Linux and macOS.
 1. Download and install OpenSesame 3.1 at [http://osdoc.cogsci.nl/3.1/download/](http://osdoc.cogsci.nl/3.1/download/)
 1. Download latest version of experiment here on GitHub or by you Git client
 1. Open downloaded experiment in OpenSesame (*.osexp)
 1. Run experiment with ctrl + R (Windows, probably Linux) or ⌘ + R (macOS)

# Paradigm scheme
| Screen name  | Description                             | Type      | Duration | Log              | Name        |
|--------------|-----------------------------------------|-----------|----------|------------------|-------------|
| Fish cluster | Main experimental stimuli               | Sketchpad | 1500 ms  | Onset            | FishCluster |
| Blank answer | Blank black screen with + with response | Sketchpad | infinite | RT + FishCluster | BlankAnswer |

## Main paradigm logic
First goes interactive instructions and then practice trial on 6 basic trials which should not induce aproximal numerical system (keep that into real experimental task).

Main loop consist of fish cluster and then blank answer screen with fixation dot in it. It repeats 10 times in one block. After each 5 blocks is setted up a inter-block pause. There is presented a coin with alert sound to experimenter. It is time for participant to rest (and get motivated by coins collecting). It has to be pressed a keyboard to continue (suggested not to be done by particpant - he/she only get a mouse). After that a 1000 Hz sinus tone for 100 ms is played again. Then goes 1500 ms blank black screen to consolidate late visual components and get seamlessly ready for experiment continuing.

After main trial is finished or participant win or lose ending sequence is started. This part consists of ending sintructions, ending recording EEG.

# Debugging
In case of debugging there is variable called DEBUG in initialization sin-line script which can have only two values True/False. These sattes represent if DEBUG mdoe is on or off.

When True instuctions and practice sequence is skipped. And in BlankAnswer screen are written all parameter such as current level, current number of correct answers and number of blocks.

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
|------------------|----------------|
| EEG start        | 254            |
| EEG stop         | 255            |
| Correct answer   | 1              |
| Incorrect answer | 2              |

EEG starts after practice sequence and end after main loop finish (before ending instructions).

# Variable logging
Logfile log all kind of variables (e.g., time_xxx represent onset of particular object). Important ones are:
- LEVEL (which log difficulty level was played)
- correct (if trial was or it was not correct)
- response_time_MouseLogger (RT)
- time_FishCluster (onset of FishCluster)

# Advanced
## Another software
- Stimuli generator [https://github.com/Neurolab-JU/ans-generator](https://github.com/Neurolab-JU/ans-generator)
- Fibonacci grid calculator [https://github.com/Neurolab-JU/fibonacci-disk-grid](https://github.com/Neurolab-JU/fibonacci-disk-grid)
- Original version in presentation [https://github.com/Neurolab-JU/ans-generator](https://github.com/Neurolab-JU/ans-generator)

## Response collection
Response is done by gaming mouse with smalles possible latency (wired) which has orange and blue label on it represents buttons to press as answer on main experimental task.
- Orange - LMB
- Blue - RMB
