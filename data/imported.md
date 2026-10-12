Skip to main content

⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-
dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).

[![Flet](/img/flet-logo.svg)![Flet](/img/flet-logo-
dark.svg)](/)[Docs](/docs)[Gallery](https://studio.flet.dev/gallery)[Studio](/studio)[Pricing](/pricing)[Roadmap](/roadmap)[Blog](/blog)

[☆Star](https://github.com/flet-dev/flet "GitHub repository")

Search

[ Meet Flet 1.0 ↗](/blog/flet-1-0)

# Your next app.  
Built in Python.

Build beautiful web, desktop, and mobile apps from one Python codebase.

[Try online ↗](https://studio.flet.dev)[Read the docs →](/docs)

No frontend experience required. Just Python.

● ● ●My first Flet app↗

![A to-do app built with Flet, with editable tasks and completion
filters](/img/blog/declarative-ui/todo.png)

![Flet Gallery running on an iPhone](/docs/assets/getting-started/testing-on-
mobile/ios/gallery.png)

[Real apps. All Python. ↗](https://github.com/flet-dev/awesome-flet)

One codebase.  
**Make yourself at home.**

  * iOS
  * Android
  * Windows
  * macOS
  * Linux
  * Web

A SIMPLE EXAMPLE

## Your first Flet app.

Start with a simple counter to see how Flet turns Python code into an
interactive app.

  1. ### Build the interface

Use ready-made controls for the text and button. Arrange them with Python.

  2. ### Add the behavior

Connect the button to a Python function that increases the count.

TRY IT YOURSELF

[Try online ↗](https://studio.flet.dev/gallery/getting-
started/example/apps/templates/basic_counter)

Open Flet Studio.  
No installation needed.

[Try locally ↗](/docs/getting-started/installation)

Follow the installation guide for uv or pip.

counter.py

ImperativeDeclarative

Imperative: update the controls directly when the button is clicked.

[Compare the two styles ↗](/docs/cookbook/declarative-vs-imperative)

    
    
    import flet as ft  
    
    
      
    
    
      
    
    
    def main(page: ft.Page):  
    
    
        counter = ft.Text("0", size=50, data=0)  
    
    
      
    
    
        def increment(e):  
    
    
            counter.data += 1  
    
    
            counter.value = str(counter.data)  
    
    
      
    
    
        page.floating_action_button = ft.FloatingActionButton(  
    
    
            icon=ft.Icons.ADD, on_click=increment  
    
    
        )  
    
    
        page.add(  
    
    
            ft.Container(  
    
    
                content=counter,  
    
    
                alignment=ft.Alignment.CENTER,  
    
    
                expand=True,  
    
    
            )  
    
    
        )  
    
    
      
    
    
      
    
    
    ft.run(main)  
    

$ flet run counter.py

BUILT FOR THE WHOLE JOURNEY

## More than a pretty interface.

The controls, libraries, and tools to take your app from an experiment to
something you ship.

![](/img/pages/home/controls.svg)

### Good-looking Python GUIs

150+ controls and services. Layouts, navigation, forms, and dialogs, with
customizable colors, typography, and themes.

[Explore the controls ↗](/docs/controls)![](/img/pages/home/python-
packages.svg)

### Your Python libraries. On mobile.

Bring NumPy, pandas, Pillow, and cryptography along. Prebuilt packages for iOS
and Android save you the work of compiling native dependencies.

[Browse Python packages ↗](/docs/reference/binary-packages-android-
ios)![](/img/pages/home/packaging.svg)

### Ready to ship

Package your app for desktop, mobile, and web with flet build. Prepare it for
distribution, including the App Store and Google Play.

[Build and publish ↗](/docs/publish)![](/img/pages/home/web-support.svg)

### The web, your way

Run Python in the browser with Pyodide and WebAssembly, or keep your code on a
server and send real-time UI updates.

[Explore web deployment ↗](/docs/publish/web)![](/img/pages/home/app-
testing.svg)

### Test your app

Write pytest tests that tap buttons, enter text, and check user flows in your
packaged app. Catch visual changes with screenshots on iOS and Android.

[Test your app ↗](/docs/getting-started/integration-
testing)![](/img/pages/home/ai-assistance.svg)

### Give your AI the right context

Connect your coding assistant to Flet MCP for version-specific API information
and tools to find examples, icons, and CLI options.

[Connect Flet MCP ↗](/docs/cookbook/flet-
mcp)![](/img/pages/home/extensible.svg)

### Make it your own

Compose custom controls in Python or wrap Flutter packages in extensions to
add new UI components and platform integrations.

[Build an extension ↗](/docs/extend/user-
extensions)![](/img/pages/home/accessible.svg)

### Build for more people

Support screen readers with labels and custom semantics. Add keyboard
shortcuts and inspect the accessibility information your UI exposes.

[Explore accessibility ↗](/docs/cookbook/accessibility)

MEET FLET STUDIO

## An idea is a  
great place to start.

Open your browser. Pick an example, write some Python, or ask the AI agent for
a hand. Run your app and share what you make.

[Create in Studio ↗](https://studio.flet.dev)No installation required.

01

### Find your starting point

Explore the Gallery and make an example your own.

02

### Make it work your way

Edit the code, get help from AI, and see your app run.

03

### Share what you made

Send a link, or download your project and keep building locally.

[Explore the Gallery ↗](https://studio.flet.dev/gallery)

MADE BETTER, TOGETHER

## Your app. Our community.

Share an idea, ask a question, or help shape what comes next. Flet is open
source, and you're invited.

[Contribute on GitHub ↗](https://github.com/flet-dev/flet)[Join us on Discord
↗](https://discord.gg/dzWXP8SHG8)[Discover community projects
↗](https://github.com/flet-dev/awesome-flet)

Loading...

Docs

  * [Introduction](/docs)
  * [Reference](/docs/reference)

Studio

  * [Flet Studio app](https://studio.flet.dev)
  * [Pricing](/pricing)
  * [Docs](/docs/studio)
  * [What's new](/docs/studio/whats-new)

Community

  * [Discord](https://discord.gg/dzWXP8SHG8)
  * [Stack Overflow](https://stackoverflow.com/questions/tagged/flet)
  * [X](https://x.com/fletdev)
  * [Bluesky](https://bsky.app/profile/fletdev.bsky.social)

More

  * [Blog](/blog)
  * [GitHub](https://github.com/flet-dev/flet)
  * [Support](/support)

Legal

  * [Privacy policy](/privacy-policy)

Copyright © 2026 Appveyor Systems Inc. Built with Docusaurus.

