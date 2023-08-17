[![2023 PyIT 🇮🇹 generate gallery.pdf](https://github.com/Kislovskiy/talks/actions/workflows/2023-PyConIT-workflow.yml/badge.svg)](https://github.com/Kislovskiy/talks/actions/workflows/2023-PyConIT-workflow.yml)

# The bumps in the road: A retrospective on my data visualisation mistakes

## TL;DR

* 🚀 Applying software engineering best practices can significantly improve productivity in data visualisation projects.
* 🤝 Collaborative efforts can expedite value creation.
* 🔬 Striving for reproducibility guarantees accuracy and consistency in the visualisation outcomes.
* 💾 Backing up data is crucial to avoid the loss of significant information.
* 🗂️ Version Control aids in meticulous change tracking and facilitates reverting to previous versions when required.
* 🕵️‍♀️ Setting up monitoring is essential for swift detection and resolution of errors or issues.
* 🚚 Establishing a continuous delivery pipeline ensures efficient and prompt delivery of data visualisations to
  customers.

To start:

```
python -m venv .venv
source .venv/bin/activate
```

## General stracture of the project

```
.
├── .github
│  └── workflows
│     └── 2023-pycon-de-python-pdf-workflow.yml
├── 2023_PyData_Berlin
│  ├── data
│  ├── requirements.txt
│  ├── README.md
│  ├── results
│  ├── src
│  │  ├── assemble_plots.py
│  │  ├── less-is-more.py
│  │  ├── plot_common_chart.py
│  │  ├── plot_cos.py
│  │  ├── plot_data.py
│  │  ├── plot_nothing.py
│  │  ├── plot_sin.py
│  │  ├── plot_text.py
│  │  ├── plotting_utils.py
│  │  ├── suboptimal_code
│  │  │  ├── chart.ipynb
│  │  │  ├── missleading.ipynb
│  │  │  └── sin.ipynb
│  │  └── transform_data.py
│  └── tests
│     ├── test_data.py
│     ├── test_plot_cos.py
│     └── test_transform_data.py
└── LICENSE
```

# gallery of plots

### Plot text

![static](results/static.svg)
![dynamic](results/dynamic.svg)

### Common chart components

![common chart](results/common_chart.svg)

### Same data different colormaps

![cmap_waves](results/cmap_waves.svg)

### Don't trust the defaults

![missleading_charts](results/missleading_charts.svg)

### Sine

![sine](results/sin.svg)

### Cosine

![cosine](results/cos.svg)

# Transcript

**The bumps in the road: A retrospective on my data visualisation mistakes**

## Slide 1

Hi, I am Artem Kislovskiy a software engineer at day and physicist at night.
Past 8 years I've been working on data visualisation projects in different domains, starting from Computational Fluid
Dynamics, to Business Analytics.

## Slide 2

When I first started a data visualisation project I was very excited, and thought that it would be a piece of cake.
As you may deduce from the title of my talk, it was not the case. The bumps in the road were many, and the journey was
turbulent.

## Slide 3

When I look back at my journey, I see that I didn't know the rules for better data visualisations.
I spent too much time on the wrong things, and I didn't have a clear vision of what I was trying to achieve.
I was completely lost in how to use version control for my plotting code, which ended up in a mess of notebooks and
scripts.
I was sure that visualisations are unbreakable, and I didn't have a backup plan.
I made a mistake of not setting up monitoring, and I didn't discover the problem until it was too late.
But I've learned a lot, and I want to share my experience with you.

## Slide 4

I am very easy to inspire, and when someone talks about data visualisation it's hard for me to resist.
I want to start coding right away.
I draw colourful images in my head, and I want to see them on the screen.
I can spend hours on prettifying the plot and making it look nice.
However, I've learned that it's not the best way to start a data visualisation project.
Often, people have completely different expectations of what the visualisation should look like.
Maybe they even don't need a visualisation at all.
In some cases they need an interactive dashboard, in other cases they need a report, and in some cases they need to
learn something from the data.
I love matplotlib, most of the graphs I've made for this presentation were made with it, but it's not the best tool for
every job.
But I'll stick to matplotlib for this presentation, because it's the most popular tool for data visualisation.
It also teaches to apply object-oriented approach to data visualisation.

Static visualisations are usually created for reports, and they are awesome for communicating results.
Dynamic visualisations usually created for interactive dashboards, and they are very helpful in exploratory data
analysis.

But remember before coding anything, you need to have a clear vision of what you are trying to achieve.
That's why the first graph I make is always the one drawn on a piece of paper.
Think how you need to display the data to answer the question.
If you were to compare two different configurations of the application deployed for A/B testing, you would probably want
to see the difference between the two over time.
And line chart is a good choice for that.
Or in a different case, you may want to compare different data processing algorithms, and you'll use a bar chart for
this.
Also consider the extreme cases, for example when time of the first algorithm is significantly greater than the time of
the second algorithm.
Experiment on paper, and then you can start coding.

And again, The best visualisation software or library is the one that allows you to make the figures you need.

## Slide 5

Enough hypothetical examples, let's get to the code!
I assume that everyone in the room knows what is a version control and knows git.
If you don't, I recommend you to invest time in learning it.
Together with continuous integration principles it can automate you out of routine tasks, and it will make your life
easier.

For data visualisation projects I start simple, but you could notice a few things.
First is a directory with all the code for the project.
Second is a `.github` folder, that contains a file with a workflow for generating a `gallery.pdf` file.
The workflow is triggered when I push a commit.

## Slide 6

Continuous integration pipeline generates a gallery.pdf file with all the plots from the repository.
It's very handy to have a gallery.pdf as a reference of plots you have, but you can also see how the plots change over
time, and easily revert some of them to previous versions if necessary.
For the same reason I like to include .svg files in the README.md file, however the README could become bulky if you
have a lot of plots, that's why I prefer to have a separate file with all the plots, and in README only the most
important ones.

## Slide 7

In my projects I find myself using mostly line charts (scatter plots), bar charts, and tables.
If you remember from the list of my mistakes, I didn't know the rules for better data visualisations.
They exist, I first learned them from Nicolas P. Rougier's book "Scientific Visualisation: Python + Matplotlib", which I
highly recommend.

* Rule 1: Know Your Audience
* Rule 2: Identify Your Message
* Rule 3: Adapt the Figure to the Support Medium
* Rule 4: Captions Are Not Optional
* Rule 5: Do Not Trust the Defaults
* Rule 6: Use Color Effectively
* Rule 7: Do Not Mislead the Reader
* Rule 8: Avoid "Chartjunk"
* Rule 9: Message Trumps Beauty
* Rule 10: Get the Right Tool
  They are worth a separate talk, but we'll see them in action in the next slides.

## Slide 8

"Less is more" is the thing that I keep in mind when I'm making a plot.
The idea is that you should not try to show too much data at once, and you should not try to make your plot look too
fancy.
Let's go through the journey of transforming the graph together, by modifying the bar chart.

## Slide 9

Consider the basic line chart.

There are a couple of things that are different form the default matplotlib settings.
First you may notice that title is left aligned.
The job of the title is to accurately convey to the reader what the figure is about, what point it makes.
The y-axis label is rotated by 90 degrees, which is easier to read.
The lines are labeled directly on the plot which reduces the cognitive load.

When you're trying to show too much data at once, you may end up not showing anything.

## Slide 10

Remember everything in Python is an object, and matplotlib is no exception.
Your coding journey always starts with creating a figure and axes objects.

## Slide 11

The object-oriented approach allows you to create a function that returns a figure object.
Later you, or the CI pipeline can use this function to create a figure and add it to the gallery.
This is a good practice because it allows you to reuse the code, and it makes it easier to maintain.
At this step I want you to note a few things about the code.
As we just learned that visualisations in matplotlib are objects, we can modify them after they are created.
In this example the object that is modified a lot is the axes object, because it's the one that contains the plot.
Figure object is a container for the axes object, and it's not modified that much.

You could also notice that I like to keep my code executable, so I put the code that generates the plot in
the `if __name__ == "__main__"` block.

## Slide 12

Another argument for using data visualisation is to verify and validate numbers.
Business people for who we usually create visualisation are busy and don't have enough time to decipher a cryptic
figures.
What they want is to get a clear demonstration that something worthwhile and interesting was accomplished, they want to
see KPI's.
It's very tempting to use an average value as some sort of KPI, but it's not always the right choice.
I recently found this amazing article that shows how completely different datasets could have the same statistics.
Spend some time verifying your data pipelines.

## Slide 13

Now let's get back to structure of the data visualisation project.
The repository contains the src, tests, data, and results directories.
I prefer to use venv for managing my environments, and I use the `requirements.txt` file to specify the dependencies.

The src directory contains the python scripts for generating the plots.
It also contains the `assemble_plots.py` script that assembles all the plots into a single pdf file.
This script is called by the workflow that generates the gallery.pdf file.
Having gallery.pdf file is very handy in big projects, because it allows you to see all the plots in one place.
It also works as a test, because if you change something in the code, and the gallery.pdf file changes, you know that
something is wrong if the workflow fails.

## Slide 14

gallery.pdf is a better alternative to endless Jupyter notebooks.
I like Jupyter notebooks.
I thought that they are the best way to share results.
It was the case until I spend half a day trying to find a specific plot in a directory with a huge number of notebooks
with similar names where each notebook had lots of cells.
It was a nightmare.
I also tend to copy and paste code from one notebook to another and from one cell to another cell, and I end up with a
lot of duplicate code.
The horror was when I had to change something in the code, and I had to do it in 10 different notebooks.
At that point I thought that it's easier and faster to run a marathon than to change something in my code.
It blocked creativity and productivity.
This experience has taught me to stay away from Jupyter, however I still use it a lot for prototyping and for quick
experiments.

The better approach is to separate data processing and data visualisation.
And use object oriented approach to data visualisation.

Imagine if I need to experiment with colours and line styles, I would copy and paste this code N times to different
cells.

## Slide 15

Here is the alternative to a jupyter notebook with three cells of code to generate the plot.
You could see here what I mean by decoupling data processing and visualisation.
There are three functions.
The `plot_cmap_waves` is the one that demonstrates the decoupling of data processing and visualisation.
I have to respect only one convention in my data, it should come in a form of a pandas dataframe, and contain a column
named "X" and a column named "Y".
I can call `visuslise_curves` function 3 times with different parameters and pick the colorscheme I like.
This is a toy example, but in a real project you could find yourself in a situation where you need to experiment with
different parameters.
It's extremely easy to do it with this approach.
Having visualisations side by side is also nice, because you can compare them and see which one is better.

## Slide 16

Let's take another example why it could be useful.
It also illustrates the importance of "Do Not Trust the Defaults", and "Don't mislead the reader" rule, from the list of
rules that I showed you at the beginning of the talk.
The data is the same, but visualisation is different.
It shows the Global temperature change from 1880 to 2023.
With data, we can easily create a misleading visualisations.

But I brought this example with a purpose to demonstrate that it has the same building blocks as the previous examples.
But you've also learned the technique to experiment with data visualisations.
Everytime I define a new function, I commit changes immediately.
This gives me lots of freedom to experiment with the code, and revert changes if I don't like them, without overhead of
copying and pasting code.

# Slide 17

Tests are vitally important for data visualisation projects.
They may seem redundant, but they could save you a lot of time in a long run.
You know how your data looks like.
You could test that your processing will fail if datatypes are wrong, or if the data is missing.
You could test that your figure is not empty and contain N number of lines.

## Slide 18

When we decouple data processing and visualisation, it's easy to use a source control, like git.
But what I like the most is going back in history and seeing how the visualisation evolved.

## Slide 19

Remember I said that I made a mistake of not setting up monitoring, and I didn't discover the problem until it was too
late.
Welcome another mistake: not setting up monitoring.
I was in a situation when my processing pipeline was failing for some reason, and the dataset was incomplete.
Since it was one of many pipelines and I didn't have monitoring, I didn't notice it for a while.
It took me a week to reprocess the data, when I could have noticed the problem way earlier.
You could consider sending yourself a notification when something finished successfully, or check daily that the
datasets your visualisations are based on are up-to-date and healthy.

And as we discussed earlier you could use GitHub actions to verify the data visualisation code.
The pipeline should fail if something is wrong with the code, or tests are failing.

## Slide 20

Here is an example of assemble_plots.py script.
It could look a bit complicated, but it's not.
If you read the script from top to bottom, you will see that first we create a pdf page context, then we iterate over
the plots, and for each plot we call the plot_ function, and then we save the page.

## Slide 21

I know that some of you here could use a different programming language, or maybe using a UI tool like Tableau or
Grafana to visualise data.
Coming back to my very first story about knowing your audience, you could consider creating a duplicate of your
production dashboard and call it staging dashboard.
I find it very practical to introduce changes first in staging dashboard, discuss them with the stakeholders, and then
push them to production dashboard.

## Slide 22

Stress test your code to know the limits.
Once I found myself writing a script that was working correctly, but it was ridiculously slow.
I thought that it's fine. I'll just run it once a day.
But only after I tried to execute it on real size data, I realised that it was not only taking 10 hours to finish, but
also caused out of memory exceptions.
I had to rewrite the code to make it more efficient and learn about map-reduce paradigm. But this is another story.

## Slide 23

If I look back at my journey, I can see that many mistakes were made, but It's fine, I'm still learning.
I believe, you remember that working collaboratively is a key to success, and you could save a lot of time by
understanding what exactly you need to demonstrate with your visualisation.
When I talk about reproducibility, I want to always reproduce any of the plot's I've created in the past in the order of
minutes, not hours.
I found that Python files work best for me rather than Jupyter notebooks, but the best tool is the one with which you
are most comfortable.
Git is an absolute must-have for me, because it allows me to go back in time and see how the visualisation evolved.
Monitoring is something that gives me a piece of mind, because I know that if something goes wrong, I will be notified.
I have a separate channel in messenger tool at work where every day a number of cron jobs report the status of data
collection, data processing, and availability of datasets, I know that everything is green there, I can sleep well. If
read, I quickly go and see what's wrong.
And we looked at the example of continuous delivery pipeline, where we could use GitHub actions to verify the data
visualisation code.


