# Django-REST-Vue-CLI

This Repo Contain a Django web application with Vue CLI

# Quick Start

Follow the following steps to start this application

> ### For Windows & Mac OS

| ID  | Step                         | Instruction                                                                     |
| --- | ---------------------------- | ------------------------------------------------------------------------------- |
| 1   | Download and Install Python  | From `https://www.python.org/downloads/`                                        |
| 2   | Download and Install Node JS | From `https://nodejs.org/en/download/`                                          |
| 3   | Download and Install git     | From `https://git-scm.com/downloads`                                            |
| 4   | Clone this Repo              | command => `git clone https://github.com/mostafa201272/Django-REST-Vue-CLI.git` |

# Create Django Environment

| ID  | Step                                                       | Instruction                                                  |
| --- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| 1   | Create an Isolation Area For Project (For Production)      | `mkdir "Environment Folder name"`                            |
| 2   | Change Your current directory to the Environment directory | `cd YOUR_DIRECTORY_PATH/Environment_DIRECTORY`               |
| 3   | Install The Virtual Environment                            | `python -m venv "Environment_DIRECTORY_PATH" `               |
| 4   | Activate Environment                                       | `YOUR_DIRECTORY_PATH/Environment_DIRECTORY/Scripts/activate` |
| 5   | Upgrade pip                                                | `python -m pip install --upgrade pip`                        |
| 6   | Install Django                                             | `pip install django`                                         |
| 7   | Check the Django Version                                   | `django-admin --version`                                     |
| 8   | Install Django REST Framework                              | `pip install djangorestframework`                            |
| 9   | Deactivate the Virtual Environment (Optional)              | `deactivate`                                                 |

<hr>

# Create Django Project and add REST Framework

| ID  | Step                                        | Instruction                                                                                                                      |
| --- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Activate Environment                        | `YOUR_DIRECTORY_PATH/Environment_DIRECTORY/Scripts/activate`                                                                     |
| 2   | create django project                       | `django-admin startproject project_Name`                                                                                         |
| 3   | run django project                          | `python manage.py runserver`                                                                                                     |
| 4   | Add Django REST Framework to django project | open `settings.py` in root project folder <br> in `INSTALLED_APPS` array add the `rest_framework` and `rest_framework.authtoken` |

<hr>

# [ 2 ] Vue CLI Project Setup

> ### For Windows && Mac OS

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

> ### For **Debian-based** Linux Distributions

| ID  | Step                                                    | Instruction                                          |
| --- | ------------------------------------------------------- | ---------------------------------------------------- |
| 1   | install node JS                                         | `sudo apt install nodejs`                            |
| 2   | install node npm                                        | `sudo apt install npm`                               |
| 3   | Update System                                           | `sudo apt update`                                    |
| 4   | Upgrade System                                          | `sudo apt upgrade`                                   |
| 5   | install vue cli                                         | `npm install -g @vue/cli`                            |
| 6   | change your directory to django Application directory   | `cd APPLICATION_PATH/Django_App `                    |
| 7   | Create Vue Environment                                  | `vue create vue_env `                                |
| 8   | change directory to vue environment directory           | `cd vue_env `                                        |
| 9   | Install Vue Webpack Bundle Tracker (i.e choose version) | `npm install webpack-bundle-tracker@0.4.3`           |
| 10  | Create Vue Configuration File                           | `touch vue.config.js`                                |
| 11  | copy configurations                                     | **_show it in vue configuration file code section_** |

> ### For **RedHat-based** Linux Distributions

| ID  | Step                                                    | Instruction                                                                              |
| --- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| 1   | install node JS                                         | `sudo dnf install nodejs`                                                                |
| 2   | install node npm                                        | Should installed with step 1 command if not run this command <br> `sudo dnf install npm` |
| 3   | Update & Upgrade System                                 | `sudo dnf upgrade --refresh`                                                             |
| 4   | install vue cli                                         | `npm install -g @vue/cli`                                                                |
| 5   | change your directory to django Application directory   | `cd APPLICATION_PATH/Django_App `                                                        |
| 6   | Create Vue Environment                                  | `vue create vue_env `                                                                    |
| 7   | change directory to vue environment directory           | `cd vue_env `                                                                            |
| 8   | Install Vue Webpack Bundle Tracker (i.e choose version) | `npm install webpack-bundle-tracker@0.4.3`                                               |
| 9   | Create Vue Configuration File                           | `touch vue.config.js`                                                                    |
| 10  | copy configurations                                     | **_show it in vue configuration file code section_**                                     |

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
