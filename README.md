# Django-REST-Vue-CLI

This Repo Contain a Django web application with Vue CLI

# Steps to Create Django application with Vue CLI

In this section we will create django project with django environment and create vue cli application with vue environment.

> ## [ 1 ] Django Project Setup
>
> > ### 1.1. Create Django Environment

> > > **1. Create an Isolation Area For Project (For Production)**
> > >
> > > > - command: `mkdir "Environment Folder name"`

> > > **2. Change Your current directory to the Environment directory**
> > >
> > > > - command: `cd YOUR_DIRECTORY_PATH/Environment_DIRECTORY`

> > > **3. Install The Virtual Environment**
> > >
> > > > - command: `python -m venv "Environment_DIRECTORY_PATH" `

> > > **4. Activate Environment**
> > >
> > > > - command: `YOUR_DIRECTORY_PATH/Environment_DIRECTORY/Scripts/activate`
> > > > - **_OR_**
> > > > - Change your current directory to environment Scripts Folder and activate
> > > >   > 1. command: `cd YOUR_DIRECTORY_PATH/Environment_DIRECTORY/Scripts/`
> > > >   > 2. command: `activate`

> > > **5. Upgrade pip**
> > >
> > > > - command: `python -m pip install --upgrade pip`

> > > **6. Install Django**
> > >
> > > > - command: `pip install django`

> > > **7. Check the Django Version**
> > >
> > > > - command: `django-admin --version`

> > > **8. Install Django REST Framework**
> > >
> > > > - command: `pip install djangorestframework`

> > > **9. Deactivate the Virtual Environment**
> > >
> > > > - command: `deactivate`

<hr>

> > ### 1.2. Create Django Project and add REST Framework

> > > **1. Activate Environment**
> > >
> > > > - command: `YOUR_DIRECTORY_PATH/Environment_DIRECTORY/Scripts/activate`
> > > > - **_OR_**
> > > > - Change your current directory to environment Scripts Folder and activate
> > > >   > 1. command: `cd YOUR_DIRECTORY_PATH/Environment_DIRECTORY/Scripts/`
> > > >   > 2. command: `activate`

> > > **2. Change Directory to Isolated Directory to create the project**
> > >
> > > > - command: `cd "Isolated Directory"`

> > > **3. create django project**
> > >
> > > > - command: `django-admin startproject project_Name`

> > > **4. run django project**
> > >
> > > > - command: python manage.py runserver

> > > **5. Add Django REST Framework to django project**
> > >
> > > > 5.1. open `settings.py` in root project folder
> > > > 5.2. in `INSTALLED_APPS` array add the `rest_framework` and `rest_framework.authtoken`

<hr>

# [ 2 ] Vue CLI Project Setup

> ### For Windows

| ID  | Step                                                    | Instruction                                          |
| --- | ------------------------------------------------------- | ---------------------------------------------------- |
| 1   | install node JS                                         | Download From `nodejs.org` and Install               |
| 2   | install node npm                                        | Installed with node                                  |
| 3   | install vue cli                                         | `npm install -g @vue/cli`                            |
| 4   | change your directory to django Application directory   | `cd APPLICATION_PATH/Django_App `                    |
| 5   | Create Vue Environment                                  | `vue create vue_env `                                |
| 6   | change directory to vue environment directory           | `cd vue_env `                                        |
| 7   | Install Vue Webpack Bundle Tracker (i.e choose version) | `npm install webpack-bundle-tracker@0.4.3`           |
| 8   | Create Vue Configuration File                           | `touch vue.config.js`                                |
| 9   | copy configurations                                     | **_show it in vue configuration file code section_** |

<hr>

# [ 3 ] Vue Configuration File Code

> For Windows, Linux, Mac OS

1. Change your currrent directory to `vue_env` directory.
2. Create new file called `vue.config.js`.
3. Copy next code in it

```
const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  publicPath: "http://127.0.0.1:8080/",
  outputDir: "./dist/",

  chainWebpack: (config) => {
    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: "./webpack-stats.json" }]);

    config.output.filename("bundle.js");

    config.optimization.splitChunks(false);

    config.resolve.alias.set("__STATIC__", "static");

    config.devServer
      // the first 3 lines of the following code have been added to the configuration
      .public("http://127.0.0.1:8080")
      .host("127.0.0.1")
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .disableHostCheck(true)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  }

  // uncomment before executing 'npm run build'
  // css: {
  //     extract: {
  //       filename: 'bundle.css',
  //       chunkFilename: 'bundle.css',
  //     },
  // }
};

```

<hr>

> ## [ 3 ] Linux Installation
>
> > ## 3.1. Python Requirements

> > ## 3.1. Vue CLI Requirements
