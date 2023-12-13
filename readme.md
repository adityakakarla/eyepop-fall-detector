# EyePop Fall Detector

This Python script uses EyePop.ai to detect falls.

The script takes a photo every few seconds. Each time, it identifies the biggest person. If the height of this person is greater than the width, they are standing. Otherwise, they are not standing.

If a person goes from "Standing" to "Not Standing", the script determines that the person has fallen. As a result, it plays an audio file announcing this.

## My Process

### Working With JavaScript

First, I messed around with the starter code files provided by EyePop.

I initially attempted to build a Fall Detector where users could upload content and EyePop could detect the falls. However, I noticed that my slow wifi meant the connection to EyePop kept failing whenever I sent over a video for analysis.

### Switching To Python

At this point, I decided to take inspiration from a prior computer vision project I worked on.

Instead of having a video stream running, I would take photos every few seconds. Based on the differences in the photos, I would use some sort of formula to determine if someone had fallen.

Because this would involve writing scripts and interacting with the webcam and operating system, I chose to use Python.

### My Original Idea

My original idea was fairly complex. It involved tracking the differences in y-positions to determine difference in height between photos. However, I realized this would involve a variety of calculations. Additionally, I would have had to set certain benchmarks for falling that would've been mostly random estimates.

Instead, the idea I ended up going with was easier to implement and intuitively made more sense.

### Chosen Idea

After I realized that I would have to guess formulas for whether or not a person has fallen based on body part locations, I decided to do some research online. Eventually, I found a video that mentioned a simple formula: comparing the height and width of a person to determine if they were standing.

Once I had chosen this idea, it took me an hour or so. I built my code off of the starter code + the code I had wrote for my original idea in the section above.

### Feedback

Though I had used EyePop in the hackathon I attended earlier this year, my teammates mostly dealt with configuring EyePop while I worked on connecting different APIs.

In a sense, I was still relatively new to understanding how to use the EyePop API.

I felt that the Python demo was easy to understand. I understand what each function did, and I felt comfortable interacting with EyePop with Python.

The JavaScript demo was a little trickier to understand. I couldn't figure out how to analyze videos at first. When I did, my wifi wasn't reliable enough (the connection kept breaking off after a few seconds).

### Timing

It took me longer than expected to build this out. However, that mostly came down to me being stuck on which idea to pursue.

Once I found a path that seemed suitable, it probably took me a cumulative time of 2 hours to code everything up (with help from the functions in the Python demo).

