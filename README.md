# OverTheWire - Bandit
_My solutions to the wargame "Bandit" by OverTheWire.org_

--------------------

<details>
<summary>Bandit0</summary>

  **Objective**\
SSH to the host over port 2220

**Commands:**
```
ssh bandit0@bandit.labs.overthewire.org
pw: bandit0
ls //# see contents of current directory
cat readme
```

<details>
    <summary>Bandit0 Answer</summary>
  NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
</details>
</details>

--------------------

<details>
<summary>Bandit1</summary>

  **Objective** \
Read contents of dashed filename

**Commands**
```
ls // notice the unusual file '-'
cat ./- //# command flags start with '-' so we need to specify the file path
```

<details>
    <summary>Bandit1 Answer</summary>
  rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
</details>
</details>

--------------------

<details>
  <summary>Bandit2</summary>

  **Objective** \
  Read a file with spaces in its name

**Commands**
```
ls
cat "spaces in this filename" //# OR cat spaces\ in\ this\ filename
```

<details>
    <summary>Bandit2 Answer</summary>
  aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
</details>
</details>

--------------------

<details>
  <summary>Bandit3</summary>

  **Objective** \
  Read a hidden file within `inhere` directory

**Commands**
```
ls -a inhere/ //# lists ALL files and directories in the specified path
cat inhere/.hidden
```

<details>
    <summary>Bandit3 Answer</summary>
  2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
</details>
</details>

--------------------

<details>
  <summary>Bandit4</summary>

  **Objective** \
  Read the flag from only human-readable file within `inhere` directory

**Commands**
```
ls -a inhere/
cat inhere/* //# read contents of all files within specified directory
```

<details>
    <summary>Bandit4 Answer</summary>
  lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
</details>
</details>

--------------------
