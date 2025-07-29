
# 🧪 Test Appcircle Custom Script Component

This repository includes simple scripts for testing the [Custom Script from Git Component](https://github.com/appcircleio/appcircle-custom-script-from-git-component) on Appcircle.

The script prints environment variables, handles arguments, writes to a file, and simulates failure with a special flag.

## Java Test Script

### 📦 Example Setup

```env
AC_SCRIPT_FILENAME=TestScript.java
AC_SCRIPT_REPO_CLONE_URL=https://github.com/your-org/your-repo.git
AC_SCRIPT_GIT_BRANCH=main
AC_SCRIPT_GIT_USERNAME=your-username
AC_SCRIPT_GIT_PAT=your-token
AC_SCRIPT_EXTRA_PARAMETERS=--fail
TEST_ENV_VAR=HelloFromEnv
AC_ENV_FILE_PATH=/tmp/env_output.env
```

Or, if you are using a local repository mount:

```env
AC_SCRIPT_FILENAME=TestScript.java
AC_SCRIPT_REPO_DIR=/opt/appcircle/scripts
TEST_ENV_VAR=JustTesting
AC_ENV_FILE_PATH=/tmp/env_output.env
```

### ✅ What This Script Does

* Prints all received arguments.
* Reads and prints `TEST_ENV_VAR`.
* Writes to a file named `java_output.txt`.
* Simulates a failure (exit 1) if `--fail` is provided in `AC_SCRIPT_EXTRA_PARAMETERS`.


Elbette! Aşağıda, `Appcircle Custom Script from Git Component` için farklı bir **Node.js edge case** test senaryosunu kapsayan örnek script yer almaktadır.


## Nodejs Test Script

### 📦 Example `.env` Setup for Node.js

```env
AC_SCRIPT_FILENAME=testScript.js
AC_SCRIPT_REPO_CLONE_URL=https://github.com/your-org/your-repo.git
AC_SCRIPT_GIT_BRANCH=main
AC_SCRIPT_GIT_USERNAME=your-username
AC_SCRIPT_GIT_PAT=your-token
AC_SCRIPT_EXTRA_PARAMETERS=--json={"valid":true} --fail
TEST_ENV_VAR=NodeTestEnv
AC_ENV_FILE_PATH=/tmp/env_output.env
```


### ✅ What This Script Tests

* Logs all arguments and a custom environment variable.
* Appends to the `AC_ENV_FILE_PATH`.
* Simulates failure with `--fail`.
* Validates JSON passed via `--json=...` and fails gracefully if it is malformed.


## 💍 Test Ruby Script

### 📦 Example Setup

```env
AC_SCRIPT_FILENAME=test_script.rb
AC_SCRIPT_REPO_CLONE_URL=https://github.com/your-org/your-repo.git
AC_SCRIPT_GIT_BRANCH=main
AC_SCRIPT_GIT_USERNAME=your-username
AC_SCRIPT_GIT_PAT=your-token
AC_SCRIPT_EXTRA_PARAMETERS=--fail
REQUIRED_VAR=ThisMustExist
AC_ENV_FILE_PATH=/tmp/env_output.env
```

Or, using a local directory:

```env
AC_SCRIPT_FILENAME=test_script.rb
AC_SCRIPT_REPO_DIR=/opt/appcircle/scripts
REQUIRED_VAR=TestValue
AC_ENV_FILE_PATH=/tmp/env_output.env
```

### ✅ What This Script Does

- **Checks for a required environment variable** (`REQUIRED_VAR`) and exits with error if not set.
- Prints all script arguments.
- Writes the required environment variable to a file named `ruby_env_output.txt`.
- Simulates failure (exit 1) if `--fail` is provided in `AC_SCRIPT_EXTRA_PARAMETERS`.


## 🐍 Test Python Script

### 📦 Example Setup

```env
AC_SCRIPT_FILENAME=TestScriptFailOnInvalidJson.py
AC_SCRIPT_REPO_CLONE_URL=https://github.com/your-org/your-repo.git
AC_SCRIPT_GIT_BRANCH=main
AC_SCRIPT_GIT_USERNAME=your-username
AC_SCRIPT_GIT_PAT=your-token
AC_SCRIPT_EXTRA_PARAMETERS=--fail
TEST_JSON_VAR={"key1":"value1","key2":"value2"}
AC_ENV_FILE_PATH=/tmp/env_output.env
```

Or, using a local directory:

```env
AC_SCRIPT_FILENAME=TestScriptFailOnInvalidJson.py
AC_SCRIPT_REPO_DIR=/opt/appcircle/scripts
TEST_JSON_VAR={"username":"admin","id":123}
AC_ENV_FILE_PATH=/tmp/env_output.env
```


### ✅ What This Script Does

- Prints all received arguments.
- Reads `TEST_JSON_VAR` and tries to parse it as JSON.
- Fails if the variable is missing or contains invalid JSON.
- Writes the parsed JSON keys to `python_env_output.txt`.
- Simulates failure (exit 1) if `--fail` is passed in `AC_SCRIPT_EXTRA_PARAMETERS`.


## 🧪 Test Perl Script

### 📦 Example Setup

```env
AC_SCRIPT_FILENAME=test_script.pl
AC_SCRIPT_REPO_CLONE_URL=https://github.com/your-org/your-repo.git
AC_SCRIPT_GIT_BRANCH=main
AC_SCRIPT_GIT_USERNAME=your-username
AC_SCRIPT_GIT_PAT=your-token
AC_SCRIPT_EXTRA_PARAMETERS=--fail
TEST_ENV_VAR=HelloFromPerl
AC_ENV_FILE_PATH=/tmp/env_output.env
```

Or, for a local mount:

```env
AC_SCRIPT_FILENAME=test_script.pl
AC_SCRIPT_REPO_DIR=/opt/appcircle/scripts
TEST_ENV_VAR=PerlTest
AC_ENV_FILE_PATH=/tmp/env_output.env
```

### ✅ What This Script Does

- Prints received arguments.
- Reads and prints `TEST_ENV_VAR`.
- Writes the value of the variable to `perl_output.txt`.
- Exits with failure if `--fail` is passed.


## Test Bash Script

### 📦 Example Setup

```env
AC_SCRIPT_FILENAME=test_script.sh
AC_SCRIPT_REPO_CLONE_URL=https://github.com/your-org/your-repo.git
AC_SCRIPT_GIT_BRANCH=main
AC_SCRIPT_GIT_USERNAME=your-username
AC_SCRIPT_GIT_PAT=your-token
AC_SCRIPT_EXTRA_PARAMETERS=--fail
TEST_ENV_VAR=HelloFromBash
AC_ENV_FILE_PATH=/tmp/env_output.env
```

Or, if using a local repo mount:

```env
AC_SCRIPT_FILENAME=test_script.sh
AC_SCRIPT_REPO_DIR=/opt/appcircle/scripts
TEST_ENV_VAR=BashTest
AC_ENV_FILE_PATH=/tmp/env_output.env
```

### ✅ What This Script Does

* Prints all provided arguments.
* Reads and prints the `TEST_ENV_VAR` environment variable.
* Writes the value of `TEST_ENV_VAR` to a file named `bash_output.txt`.
* Exits with error code `1` if `--fail` argument is provided, simulating failure.