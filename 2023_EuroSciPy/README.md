# Why I Follow CI/CD Principles When Writing Code: Building Robust and Reproducible Applications

The talk was given at [EuroSciPy 2023](https://pretalx.com/euroscipy-2023/talk/UBT8PH/).

## TL;DR

* Continuous Integration has become a mainstream technique for software development, but it puts together a set of
  well-defined principles and etiquette.
* Threat any project as a Python package with a well-defined structure, you'll save yourself a lot of time and headache.
* Write tests they will help you identify the right modularization of your code.
* Learn from the best, reuse the code written by others.
* If you are not using Continuous Integration I highly recommend you give it a try.

## Further Reading:

### Books

* Continuous Integration
* Robust Python
* Full Stack Testing
* Python Testing with pytest

### Articles

* [Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html)
* [Awesome Actions](https://github.com/sdras/awesome-actions)

### Videos

* [How GitHub Actions 10x my productivity](https://youtu.be/yfBtjLxn_6k)

### Transcript

Imagine a young student studying math and physics, struggling to understand why his C code is not compiling.
He's trying to finish his assignment, but he's stuck.
He was alone and there's no one to help him.
Programming was always hard to me, I was never a good programmer.

When I look back I can see that I've made a lot of mistakes, and I'm still making them.
But I'm very happy that at my first software engineering job I was introduced to Continuous Integration.
It made my life easier, and programming more fun.

This talk is about Continuous Integration and Continuous Delivery, which become essential to software development.
It removed a lot of unnecessary mental burden from me, I'm not afraid to make changes to the code, and I'm not afraid to
break it.

If you never heard about Countinuous Integration, in short this practice is about the workflow that makes everything
easier.
It can be easily split into seven steps.

1. code locally on a feature branch
2. open a pull request
3. run automated tests
4. if tests pass, manually merge
5. once merged, run automated tests again
6. push the conterized application to a registry
7. distribute the code

In my opinion the last point is the most important one.

*Dress for the job you want, not the job you have.*

Python packaging is tricky, there are many materials about it, and what was once considered good practice is now
outdated.
The best way to learn is to look at the code written by others, however it could be challenging for a beginner.
As with every Python project, you should follow roughly the same steps when you start, which include making a new
directory and then creating and activating an isolated virtual environment for your project.
And it starts with the project structure, there are many good templates for python project, don't reinvent the wheel
use them. e.g. https://github.com/rochacbruno/python-project-template
From the good intentions, if you already have a project you are actively working on, review the template and refactor
it.
And that's where having Continuous Integration in place helps a lot and the steps of commiting a small changes to the
project and running automated test suit become very handy.

The Python official documentation has a great tutorial on Packaging Python
Projects: https://packaging.python.org/en/latest/tutorials/packaging-projects/

When you are done with the tutorial you'll end up with the following project structure:

```shell
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── example_package_YOUR_USERNAME_HERE/
│       ├── __init__.py
│       └── example.py
└── tests/
    └── test_example.py
``` 

And there are a lot to talk about here.
First is a `pyproject.toml`. TOML is a configuration file format that has gained popularity lately.
Starting with PEP 621 (https://peps.python.org/pep-0621/), the Python community selected pyproject.toml as a standard
way of specifying project metadata.
In general, TOML files contain key-value pairs separated into sections, or tables.
[Configuring setuptools using pyproject.toml files](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
is a good place to start, but it may look a bit overwhelming at first, but don't panic and read it carefully, you'll
understand that for the simple project as yours it would be enought to have the following:

```toml
[build-system]
requrires = ["setuptools", "setuptools-scm"]
build-backend = "setuptools.build_meta"

[project]
name = "packaging_tutorial"
version = "0.1.0"
```

After you've done this you can install your project to be available enywhere.

```shell
python -m pip install --editable
```

I really wish I could learn this earlier, this will save me a lot of energy and time.

Second thing that people usually not focus on is the right pick of licence.
It's importand because it defines how others can use your code.

Here is some examples from popular Python projects:

* First off, SymPy is completely free. It is open source, and licensed under the liberal BSD license, so you can modify
  the source code and even sell it if you want to (https://docs.sympy.org/latest/tutorials/intro-tutorial/intro.html)
* Distributed under a liberal BSD license, NumPy is developed and maintained publicly on GitHub by a vibrant,
  responsive, and diverse community. (https://numpy.org/)

You can refer to: https://choosealicense.com/
Or follow Anwesha Das, who does a great job educating community about right pick of licence for your projects
e.g. https://anweshadas.in/my-talk-about-software-licenses-in-pycon-india/

It might look as a lot of information and it is.
If your existing codebase doesn't allow you to experiment with this quickly, maybe it would be a good idea to set up a
small toy project and play with it.
It's a great way to learn and it's fun.

> Maybe it would be a good idea to continue setting up the Continuous Integration on this small project.

Finally, we are ready to talk about Continuous Integration.
There is another rabbit hole for the beginners on this way is a knowledge of Git and GitHub, I'll skip this step for now
and will refer to the amazing resources that you can find following this link.

Let's revert back to what we've started with.

1. code locally on a feature branch
2. open a pull request
3. run automated tests
4. if tests pass, manually merge
5. once merged, run automated tests again
6. push the conterized application to a registry
7. distribute the code

And introduce GitHub Actions.
As a disclaimer, there are other great products that have the same functionality, I picked GitHub Actions because it's
well integrated with your GitHub repository and allow to do a great things.

But first what is GitHub Actions?
When you host your code in a repository on GitHub there is a ton of different events that could happen.
For example, someone can push some new code to the main branch, or another person can open a pull request, or maybe
someone opens an issue because your code is not working as expected.
There is a big list of events that can happen to a repository, and Action listens to these events and can trigger some
code to run automatically when they happen.
In the background GitHub spins up a magical cloud virtual environment build according the specifications and runs the
code you've defined.
It's a great way to automate routine tasks.
Of course running things in a Cloud costs money, but GitHub Actions has a amazing free tier that most projects won't
probably exceed.

Why do we need Continuous Integration?
One of the common tenets of the DevOps mindset is to “shift your errors left.”
The idea is to think of your errors in terms of their cost. How expensive is it to fix an error?
The earlier in the development cycle you are, the less expensive it is to address errors.

To get started we need to create a `.github` directory in the root of our project, followed by a `workflows` directory.
As with many tools related to DevOps these days, GitHub uses the YAML format for configuring workflows.
Then inside we create a yaml file that can be named whatever you want.

You can logically split every workflow file into three sections:

* name of the workflow
* when to trigger the workflow
* what to do when the workflow is triggered

Most of the time your file will look something like this:

```yaml
# .github/workflows/ci.yml

name: "Continuous Integration"
run-name: "️CI for (${{ github.sha }})"

on:
  pull_request:
    branches:
      - main
  push:
    branches:
      - main
  workflow_dispatch:

defaults:
  run:
    shell: bash -e {0}

jobs:
  build:
    name: Build with Python ${{ matrix.python-version }} on ${{ matrix.os }}
    runs-on: ${{ matrix.os }}

    strategy:
      fail-fast: false
      matrix:
        os: [ macos-latest, ubuntu-latest, windows-latest ]
        python-version: [ "3.9", "3.10", "3.11" ]

    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
```

Without even diving deep you could imitatively notice some of awesome things that could help you to increase
maintainability of your codebase.

Back in a day when I was a student it was so painful to collaborate with my peers because usually any software that I or
they wrote were coupled with their local environment and OS.

The problem with this approach is that everyone on the team works on their own copy of the project.
The longer the integration phase is delayed, the more likely it is that the different versions of the project will
diverge, making it difficult to combine them.
In some cases, integration could take more time than the actual development of the project!

With GitHub Actions you can easily set up a matrix of different OS and Python versions to run your code on.
Alternatively you can learn how to develop and package your code in a container and run it in a containerized
environment, but this is a topic for another day.

With the current setup we prepared the environment we need to decide what to do next.
First of all, we should clean up your code by formatting it consistently, sorting the import statements, and checking
for PEP 8 compliance.
We can achieve this by using a class of static analysis tools called linters.
Linters search for common programming mistakes and style violations within your codebase.
They get their name from the original linter: a program named lint that used to check C programs for common errors.

As author of "Robust Python" book writes in the charapter about Static analysers.
There are many static analysis tools available for Python.
Often each tool you use builds a safety net for a different class of errors.
For example, typecheckers won't catch common programming mistakes, linters won't check security violations, security
checkers won't catch complex code, and so on.
But when these tools are stacked together, it's much less likely for a legitimate error to get through.

As a minimum you'll use black to flag any formatting inconsistencies in your code, isort to ensure that your import
statements stay organized according to the official recommendation, and flake8 to check for any other PEP 8 style
violations.

Finally, it’s too common to inadvertently leak sensitive data through your source code or expose other security
vulnerabilities.
It happens even to the best software engineers.
Recently, GitHub exposed its private key in a public repository, which could’ve allowed attackers to impersonate the
giant. (https://github.blog/2023-03-23-we-updated-our-rsa-ssh-host-key/#what-happened-and-what-actions-have-we-taken)
To reduce the risk of such incidents, you should perform security or vulnerability scanning of your source code before
deploying it anywhere.

```yaml
jobs:
  lint:
    name: 🚨 Lint Python code
    runs-on: ubuntu-latest
    steps:
      - name: Setup Python environment
        uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      - name: Install dependencies
        run:
          pip install -r 2023_PyData_Berlin/requirements.txt
      - name: Run Black
        run:
          black 2023_PyData_Berlin --check
      - name: Run Flake8
        run:
          flake8 --config 2023_PyData_Berlin/.flake8 2023_PyData_Berlin
```

Testing

When it comes to writing unit tests, it’s quite common for those in the Python community to choose pytest over the
standard library’s unittest module.
Thanks to the relative simplicity of pytest, this testing framework is quick to start with.

When we've done with setting up our Continuous Integration pipeline we have some confidence that our robots will do the
routine work of checking the code style and running tests for us.
There is another bit that we could ask robots to do for us, is to automatically check the versions of our dependencies
and update our codebase when they are available.

There are two common applications that could be used for this: Renovate and Dependabot.
And as almost everything in a DevOps world is configured in yaml's these tools are not an exception, but they can
improve your code without you doing anything.
Usually newer versions of libraries contain some fixes or performance optimisations that could make your code better.

I use Renovate, because it's highly customizable (https://github.com/renovatebot/renovate). After you've installed this
GitHub App it will open a first PR with a configuration file that you can tweak to your needs.
Now your dependencies will be updated automatically, and you'll be notified about it in a PR.

Now it's time to wrap up and remind you about the main points of this talk.

We've talked about Continuous Integration, and we saw that there are many things that make your project easier to
maintain and collaborate on.
I had time to touch only a part of fascinating world of software development, but I encourage you to explore it further,
play with it, and make fun of it.
In the end even a small step in the right direction is better than nothing.
Not always we have a privilege of having someone who can review our code and catch errors, but as I showed in the
example of GitHub Actions we can make robots do some of the routine work for us, and ensure that on every commit our
code is tested and checked.

I wrote an extensive resource list for this talk that you can find here, and if you feel inspired but overwhelmed and
struggle to identify the first step that you could take for your project, I am always more than happy to help you with
that.

There are many good books and articles about it, you can find them in the resource section of this talk.
It looks simple, but as I said, programming was always hard to me.
And I believe it is for many of us here.

My goal today to share not the best practices, but share better practices.
And the first thing that comes to mind is automation.
Seek for opportunities to automate your routine tasks.
Let's start with your code repository and the project structure.

Every Python project

*Dress for the job you want, not the job you have.*
As with every Python project, you should follow roughly the same steps when you start, which include making a new
directory and then creating and activating an isolated virtual environment for your project.
And it starts with the project structure, there are many good templates for python project, don't reinvent the wheel
use them. e.g. https://github.com/rochacbruno/python-project-template
If you already have a project you are actively working on, review the template and refactor it.

Using a pyproject.toml file and creating an editable install may sound like something you might only need when
distributing you package.
However it's something that will make developing anything larger than a single file script much easier and less
headache-prone.

The next usually ignored aspect is a licence for your code.
It's importand because it defines how others can use your code.
You can reffer to: https://choosealicense.com/
Or follow Anwesha Das, who does a great job educating community about this
e.g. https://anweshadas.in/my-talk-about-software-licenses-in-pycon-india/

The most important documents that define how Python packaging works are the following PEPs:

    PEP 427 describes how wheels should be packaged.
    PEP 440 describes how version numbers should be parsed.
    PEP 508 describes how dependencies should be specified.
    PEP 517 describes how a build backend should work.
    PEP 518 describes how a build system should be specified.
    PEP 621 describes how project metadata should be written.
    PEP 660 describes how editable installs should be performed.

https://packaging.python.org/en/latest/tutorials/packaging-projects/

Arguments for licence:

* First off, SymPy is completely free. It is open source, and licensed under the liberal BSD license, so you can modify
  the source code and even sell it if you want to (https://docs.sympy.org/latest/tutorials/intro-tutorial/intro.html)
* Distributed under a liberal BSD license, NumPy is developed and maintained publicly on GitHub by a vibrant,
  responsive, and diverse community. (https://numpy.org/)

For Testing:

* https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

For publishing:

* https://olgarithms.github.io/sphinx-tutorial/docs/8-automating-documentation-updates.html

### Robust Python

#### Chapter 20. Static Analysis

> Static analysis is a set of tools that inspect your codebase, looking for potential errors or inconsistencies. It’s a
> great asset for finding common mistakes. In fact, you’ve already been working with a static analysis tool: mypy. Mypy (
> and other typecheckers) inspect your codebase and find typing errors.

**Linting**
The first class of static analysis tools that I’ll walk you through is called a linter. Linters search for common
programming mistakes and style violations within your codebase. They get their name from the original linter: a program
named lint that used to check C programs for common errors.

TODO: setup MyPy and Pylint (?)

One of the common tenets of the DevOps mindset is to “shift your errors left.” I mentioned this when discussing types,
but it applies to static analysis and tests as well. The idea is to think of your errors in terms of their cost. How
expensive is it to fix an error? It depends on where you find that error. An error found in production by a customer is
costly. Developers have to spend time away from their normal feature development, tech support and testers get involved,
and there are risks when you have to do an emergency deployment.

The earlier in the development cycle you are, the less expensive it is to address errors. If you can find errors during
testing, you can avoid a slew of production costs. However, you want to find these issues even earlier, before they ever
enter into the codebase. I talked at length in Part I about how typecheckers can shift those errors even further left,
so that you find the errors right as you develop. It’s not just typecheckers that allow you to do this, but static
analysis tools such as linters and complexity checkers as well.

Typecheckers and linters are often the first things people think of when they hear “static analysis,” but there are so
many additional tools that can help you write robust code.

Likewise, each tool you use to build a safety net will miss certain errors. Typecheckers won’t catch common programming
mistakes, linters won’t check security violations, security checkers won’t catch complex code, and so on. But when these
tools are stacked together, it’s much less likely for a legitimate error to squeak by (and for those that do, that’s why
you have tests). As Bruce MacLennan says, “Have a series of defenses so that if an error is not caught by one, it will
probably be caught by another.

“Where can I find the most bugs in my code?” Most of the time, it will be in code with high complexity, but remember
that this is not a guarantee.

You can use a static analysis tool in Python to measure cyclomatic complexity, aptly named mccabe.

Whitespace heuristic

There’s another complexity heuristic that I am quite fond of that is a bit simpler to reason about than cyclomatic
complexity: whitespace checking. The idea is as follows: count how many levels of indentation there are in a single
Python file. High levels of indentation indicate nested loops and branches, which may signal complex code.

You’ll learn how to graph your dependencies, and how to interpret whether you have a healthy system. You’ll learn how to
truly simplify your code architecture, which will help you manage complexity and increase the robustness of your
codebase. It doesn’t make sense in most codebases to write literally everything from scratch. Reusing other parts of the
codebase, or even code from other organizations, can be immensely beneficial.

Dependencies also broaden the attack surface from a security perspective. Every dependency (and their own dependencies)
has potential to compromise your system. There are entire websites dedicated to tracking security vulnerabilities, such
as https://cve.mitre.org. A keyword search of “Python” shows you how many vulnerabilities exist today, and naturally,
those websites can’t even count the not-yet-known vulnerabilities.

If you foresee the need to change the pinning of a dependency, you need a strategy for updating those dependencies. I
recommend keeping the dependencies pinned, but lean on a continuous integration workflow and dependency managers such as
poetry to update those dependencies. With continuous integration, you are constantly scanning for new dependencies. When
dependencies change, the tools will update the dependencies, run tests, and if tests pass, check in the new pins for the
updated dependencies. This way, dependencies stay up to date, but you always maintain a checked-in set of pins for
reproducibility. The downside here is that you need to have the discipline and supporting culture to fix the failed
integrations as they appear. Tackling failures piecemeal is much less effort in the long run than delaying the
integration.

Visualizing Packages

pip install pipdeptree graphviz
pipdeptree --graph-output png --exclude pipdeptree,graphviz > deps.png

Visualizing Imports

Visualizing packages is quite a high-level view, so it helps to go one step deeper. How can you find out what’s being
imported at the module level? Another tool, called pydeps, is great for this.

Visualizing Function Calls

If you want even more information than an import graph, you can see which functions call each other. This is known as a
call graph. First, I’ll look at a static call graph generator. These generators look at your source code and see which
functions call which; no code is executed. For this example, I’ll use the library pyan3, which can be installed with:

pip install pyan3

### Full Stack Testing

Testing is one of the componet's of CI/CD pipelines. Continious Testing.
> The CT process relies heavily on the practice of continuous integration (CI) to perform automated testing against
> every change. Adopting CI together with CT allows the team to do continuous delivery (CD). Ultimately, the trio of CI,
> CD, and CT make the team a high-performing one, as measured by the four key metrics, lead time, deployment frequency,
> mean time to restore, and change fail percentage.

> Martin Fowler, author of a half dozen books including Refactoring: Improving the Design of Existing Code (Addison
> Wesley) and Chief Scientist at Thoughtworks, describes continuous integration as “a software development practice where
> members of a team integrate their work frequently, usually each person integrates at least daily—leading to multiple
> integrations per day.” Let’s consider an example to illustrate the benefits of following such a practice.

> Two teammates, Allie and Bob, independently started developing a login and home page. Work started in the morning, and
> by noon Allie had finished a basic login flow and Bob had completed a basic home page structure. They both tested their
> respective functionalities on their local machines and continued work. By the end of the day, Allie had completed the
> login functionality by making the application land on an empty home page after successful login, since the home page
> wasn’t available to her yet. Similarly, Bob completed the home page functionality by hardcoding the username in the
> welcome message, since the user information from the login was not available to him.

> The CI/CT process relies on four individual components:

    The version control system (VCS), which holds the entire application code base and serves as a central repository from which all team members can pull the latest version of the code and where they can integrate their work continuously

    The automated functional and cross-functional tests that validate the application

    The CI server, which automatically executes the automated tests against the latest version of the application code for every additional change

    The infrastructure that hosts the CI server and the application

> the team members follow a set of well-defined principles and etiquette.

### The DevOps Handbook

Highlights the importance of observability.

### Beyond Fireship

[How GitHub Actions 10x my productivity](https://youtu.be/yfBtjLxn_6k)

Many years ago A wise man once told me why spend five minutes doing something when you could spend five hours failing to
automate it.
One of the secrets to productivity in life is automation. As I flow through life I try to delegate anything repetitive
to the robot so I can focus on the things that are really important in life. When it comes to automating software
development my favorite continuous integration and delivery tool is GitHub actions. Recently I've been working on
getting an npm package called spell fire production ready and in today's video I'll show you how I save tons of time by
automating this project. But first what even is a GitHub action well when you host your code in a repository on GitHub
there's a ton of different events that can take place like you might push some new code to the main branch or another
user might do a pull request to merge changes into your code or maybe someone opens up an issue because your code sucks
there's a huge list of potential events that can happen to a repo Now with an action you can trigger some code to run
automatically when one of these events take place in the background GitHub will spin up a magical Cloud computer also
known as a container that's built to your specifications and runs your code to automate things like testing deployment
and so on Computing things in the cloud of course costs money and is build per minute but GitHub has a generous free
tier that most projects won't exceed to get started just create a hidden GitHub directory in the root of your project
followed by a workflows directory then inside of that create a yaml file that can be named whatever you want now before
we create our first workflow there's one project that I would highly recommend you install called act this is a CLI tool
that will emulate GitHub workflows for you so you can test them locally you'll also need to have Docker installed and
running because what it does is build out an actual container just like it does in the cloud with GitHub actions if you
don't have Docker on your machine the easiest way to get it is to install Docker desktop once you have act installed you
can run the ACT command which by default will emulate an on push event to run any workflows that are tied to pushing
code to the repo you can of course customize the event to test different workflows or just run the workflows
individually now we're ready to Define our first workflow which will test our code automatically writing tests for your
code is never an absolute requirement but when building a library like spellfire for other people to use it's extremely
important not only will testing help prevent bad code from getting into a release but it also makes your life way easier
when you have other people contributing to the project with GitHub actions we can automatically run our tests in the
cloud and we'll know immediately whenever a pull request comes through if that contributor broke the existing code this
Project's actually somewhat difficult to test because it deals with cloud data but currently we have playwright tests in
place which allow us to test the code in a simulated browser environment now let's go ahead and set up a workflow to run
the test automatically in the cloud first you give the workflow a name just to identify it then most importantly the on
property will tell GitHub on which events to run this action in our case we want to test our code whenever we push it to
the main or Master Branch however we also want to test code whenever a pull request comes through that's requesting to
merge code into the master Branch now that we have our events configured we can Define one or more jobs which is the
actual code that will run in the cloud give it a name like build and then specify an operating system for it to run on
like Ubuntu is usually the best default one cool side note here though is that you can also use a matrix strategy to run
your jobs in multiple environments like Windows and Linux it's not really important in our case but it's a good thing to
know now every workflow job is broken up into a series of steps and this is the part where we tell the robots how to do
the things that we would otherwise have to do manually the first step uses the uses option which is a keyword that
allows us to use pre-built steps like checkout will bring the code from the repository into the container and then set
up node We'll add node.js and npm to your path I'm also using the width keyword to specify node 18. now that we have an
environment set up the way we need it we can use npmci which is the equivalent to npm install but does a clean install
which is what you want for automated environments and then when it comes to playwright it recommends using npx instead
of your local binaries so we'll go ahead and do that for the install and the testing of playwright and that's really all
there is to it we now have automated testing set up on this project now go ahead and run the ACT command and it should
build out the container and test your code locally one other cool thing I want to show you though when it comes to
playwright is that there's another step we can use called upload artifact what this will do is save the playwright
report as an artifact in the GitHub actions environment that means if your tests do fail you can go into the artifacts
and get a detailed report of what went wrong and then they'll be automatically deleted after 30 days now that we have
automated testing in place let's take a look at automated deployment many hosting platforms like versel and netlify do
this for you automatically nowadays but it's super easy to do on your own with spillfire I'm building a dedicated
documentation website with Astro now anytime anything changes on the master Branch we want the documentation to
automatically update and redeploy to Firebase hosting now the documentation website is basically its own isolated
project in this docs directory so in the workflow we're going to set the default working directory to the docs directory
that means in our build steps when it runs npmci build and deploy those commands will be run from the docs directory and
that's almost all the code we need for a deployment workflow however we can't just deploy to Firebase hosting without
being authenticated in this case we need to set up an environment variable called Firebase token but it's a super secret
value so we can't just hard code it here directly because this code will be committed to a public repo luckily we can go
on the GitHub actions dashboard and store the secret environment variable there now when this workflow runs it will have
access to that value and thus be able to deploy the site to our Firebase account and that takes care of deployment but
spillfire is an npm package and that means when we release new code we also need to publish that package to npm so
people can install it you wouldn't want to create a new package for every time code is committed to the master Branch
because a simple typofix or something wouldn't require an entirely new release a better trigger for npm publishing is
when you manually create a new release on GitHub typically what you'll do is release new version and add some notes
about the things that changed and in the background the workflow will run to publish that code on npm at the same time
like Firebase deployment it's also going to require authentication with a token and then one other thing I want to point
out here is that whenever you define a step you also have the option to give it a name as well as a few other options
beyond that given your steps a name is generally a good practice because if something goes wrong it'll be more
descriptive which makes it easier for whoever's trying to debug the workflow and when things do go wrong you get a nice
breakdown of all the logs on the GitHub actions console in rare cases and action might fail for no reason in which case
you have the option to re-run all the jobs if you suspect it was just some kind of temporary issue that should now be
resolved and that brings us to the final workflow that I want to show you this one exports data from the cloud firestore
database to a storage bucket however that event is not tied to any specific event in the code instead it happens on a
schedule which is defined with a Cron job this is really cool for any project because it makes it really easy and cheap
to run arbitrary code in the background on a specific schedule I also have workflows that generate daily reports and
things like that but you'll also notice that this particular workflow can also run on the workflow dispatch event this
allows you to manually trigger the workflow you can do it directly on the browser where I'd also recommend installing
the GitHub CLI which will allow you to trigger workflows there manually as well the GitHub CLI is cool and will allow
you to monitor things in production but it's not a replacement for act the CLI tool we looked at earlier which is more
useful when you're doing the initial setup of workflows and testing them locally to finish things off I want to give you
a bunch of examples of other workflows that you might want to set up for your projects we've already looked at testing
but another other thing you might want to do is automatically lint every pull request as well essentially this does an
automatic code review you don't have to manually go through and make sure that the code meets your stylistic standards
when it comes to maintaining a project there's all kinds of different things you can do like you can automatically Mark
issues stale if they haven't been interacted with in a long time or you can automatically label and respond to issues
which makes it look like you're actually maintaining the project even though you've already moved on to building a brand
new JavaScript framework now in some more advanced cases you may want to develop your own custom action that you can
reuse across multiple projects or publish for other people to reuse there's a project called actions toolkit that can
make that process much easier it provides all the tools you need to interact with the actions environment using
typescript before you build your own custom action though there's a good chance that somebody may have already solved
the same problem there's a repo called awesome actions that gives you a list of all the different actions and tools
available in the ecosystem now Another Thing Worth pointing out is that by default GitHub will host the actual machines
that run your code however it is possible to self-host your own Runners I've never actually done this myself but just
wanted to point it out as an option if you don't want GitHub to handle the compute which would be running on Azure Cloud
I mean who really knows what Microsoft is doing with all that code they're running in any case though GitHub actions is
an awesome platform and I would highly recommend using these free robots to get stuff done thanks for watching and I
will see you in the next one
