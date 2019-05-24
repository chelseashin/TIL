## Python Windows Local Setting

C9 서비스 종료 이슈 대응

3.7.2 가 이미 설치되어 있다면 `2. virtualenv` 로 바로 설치 가능함.

**[주의]** 이 문서는 ssafy 학생 컴퓨터를 기준으로 작성되었음. 본인의 window 컴퓨터 환경에 따라 세부적으로 달라 질 수 있음.

------

### 1. `pyenv-win`

#### 1.1 Install

<https://github.com/pyenv-win/pyenv-win>

작성일 기준 5월 현재에도 지속적으로 업데이트 되고 있음.

- SSAFY PC를 기준으로 `%USERPROFILE%` 의 path는 `C:\Users\student` 임. (대체 가능)

- 기존 파이썬이 설치 되어 있는 경우 (pip)

  ```python
  $ pip install pyenv-win --target C:/Users/student/.pyenv
  ```

- 아닌 경우 (git)

  ```python
  $ git clone https://github.com/pyenv-win/pyenv-win.git C:/Users/student/.pyenv
  ```

- 이도저도 아닌 경우(zip)

  <https://github.com/pyenv-win/pyenv-win/archive/master.zip>

  ```python
    C:/Users/student/.pyenv/pyenv-win
  ```

#### 1.2 환경변수 등록

- 윈도우에서 시스템 환경 변수 편집 선택

  - 혹은, 제어판 > 고급 시스템 설정 > 환경 변수

- 환경 변수 등록

  ```python
    %USERPROFILE%\.pyenv\pyenv-win\bin
    %USERPROFILE%\.pyenv\pyenv-win\shims
  ```

- 환경 변수 삭제 **주의!!!!!! 기존 파이썬 PATH 삭제 안하면 pyenv가 관리를 못함.** ~~윈도우ㅗ~~

  기존의 파이썬 환경변수를 모두 삭제해야 pyenv로 활용 가능함.

  시스템/사용자 환경 변수의 `Path` 에서 해당하는 내용 모두 삭제 `\pythonxx\` 임.

  아래 스크린샷에서 1, 2번째 줄임.

  [![Untitled-83e3fd38-5fac-4968-a2c0-d2bf76a9c6c9](https://user-images.githubusercontent.com/18046097/57591125-cd213700-756a-11e9-83f0-d7f8fb107721.png)](https://user-images.githubusercontent.com/18046097/57591125-cd213700-756a-11e9-83f0-d7f8fb107721.png)

- `Gitbash` 혹은 `cmd` 창을 다시 열어서 확인

  ```python
  $ pyenv --version
  ```

- 이후 동일

  ```python
  $ pyenv install 3.7.2 
  $ pyenv global 3.7.2
  $ pyenv rehash
  ```

- 설치 확인

  ```python
  $ python -V
  $ python -i
  ```

------

### 2. virtualenv

- `python 3.7.2`가 설치되어 있다고 가정 or `pyenv-win` 으로 설치

  - `gitbash` 에서 동작하게끔하려면, python 버전이 `3.7.2+` 필요

- python 내장 venv를 사용.

  - <https://docs.python.org/3/library/venv.html>

- 바탕화면에 테스트 폴더 만든 이후에 진행

- 가상환경 실행

  ```
  $ python -m venv movie-pjt
  $ source movie-pjt/Scripts/activate
  (movie-pjt) 
  $
  ```

| shell      | command                              |
| ---------- | ------------------------------------ |
| cmd.exe    | `C:\><venv>Scripts\acticate.bat`     |
| PowerShell | `PS C:\><venv>\Scripts\Activate.ps1` |
| git bash   | `<venv>\Scripts\activate`            |

- 가상환경 종료

  ```python
  $ deactivate
  ```

- pip 를 통해 정말 가상환경인지 확인

  ```python
  $ pip list
  ```

