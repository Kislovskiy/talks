# Why I Follow CI/CD Principles When Writing Code: Building Robust and Reproducible Applications

## Resources:

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
