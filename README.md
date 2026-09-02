# Xiaomi HyperOS Cookie Manager

A professional, menu-driven Python utility designed to manage session tokens and streamline local request handling for Xiaomi devices.

## Features

* **Interactive Menu System**: Easy-to-use terminal interface for session management.
* **Token Storage**: Securely parses and saves credentials (`passToken`, `cUserId`, `deviceId`) locally in JSON format.
* **Transparent Architecture**: Fully open-source and structured for educational and local lab usage.

## How It Works

This tool is designed to simplify capturing and utilizing Xiaomi account session data locally without repeatedly logging in.

### Menu Options Explained

1. **Cookie Setup (Save & View PassToken)**:
   * Prompts you to input your account credentials captured via browser tools (like Firefox Cookie-Editor).
   * **Required Cookies**: 
     * `passToken`: The core authentication token for your Xiaomi account session.
     * `cUserId` (or `userId`): Your unique account user identifier.
     * `deviceId`: The generated or bound device identifier.
   * Saves these credentials securely into a local `token.txt` file and displays a preview.

2. **Start Tool (Reuse Saved PassToken)**:
   * Reads the saved credentials automatically from `token.txt`.
   * Simulates local request handling and prepares the session for API interactions.

3. **Exit**:
   * Safely terminates the script execution.

## Installation & Setup

Clone the repository and run the setup script:

```bash
git clone https://github.com/mrrobo133/HyperOS-Cookie-tool.git
```
```bash
cd HyperOS-Cookie-tool
```
```bash
pip install colorama
```

```bash
chmod +x install.sh
```
```bash
./install.sh
```
Usage
​Run the main Python script
```bash 
python tool. py
```

### What can be done using these tokens 

* **Bootloader Unlock Request:** Sending automated requests to Xiaomi's official servers during specific windows to acquire permissions or tokens for bootloader unlocking.
* **Session Automation:** Maintaining active browser or app sessions without the hassle of repeatedly providing usernames, passwords, or OTPs.
* **API Interaction:** Establishing secure connections with Xiaomi's official backend APIs to dispatch automated requests.

