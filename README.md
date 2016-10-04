# Aproximal numerical system paradigm
<img src="https://github.com/neurolab-ju/ans-os/blob/master/stimuli/instruction_fishes.jpg?raw=true" align="right" width="350">

**Authors:**

| Name             | E-mail                     | Function    |
|------------------|----------------------------|-------------|
| Michala Plassová | michala.plassova@seznam.cz | Main author |
| Michal Vavrečka  | vavrecka.michal@gmail.com  | Supervisor  |
| Michael Tesař    | michtesar@gmail.com        | Programmer  |

**Web:**
[http://www.pf.jcu.cz/structure/departments/kpe/neurolab/](http://www.pf.jcu.cz/structure/departments/kpe/neurolab/)

**Version:**
```
1.2b
```

## How to download
First download Github desktop app or any other Git client if needed. Then download repository by git command or in any Git application by user graphical interface.

Download GitHub desktop app [here](https://desktop.github.com).
```
git clone https://github.com/neurolab-ju/ans-os.git
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
