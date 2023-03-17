# Google-meet-bot
This is a Python program that utilizes various libraries such as PyAutoGUI, PyWhatKit, and OpenCV to automate the process of joining a Google Meet session. The program is designed to help users avoid the tedious and time-consuming process of manually joining a Google Meet by performing various tasks automatically.

The program begins by defining two functions, `delay` and `wait`. `delay` is a helper function that takes a single argument, `sec`, which represents the number of seconds to wait before proceeding to the next step in the program. wait is another helper function that takes two arguments, `h` and `m`, which represent the hour and minute at which the user wishes to join the meeting. This function will wait until the current time matches the specified join time before proceeding to the next step in the program.

The `find_phNo` function searches through a CSV file called contacts.csv to retrieve a phone number associated with a given name. This is useful for sending automated WhatsApp messages to alert users of the user's arrival and departure from the meeting.

The `joinMeet` function is the main function in the program. It takes three arguments: `link`, which is the Google Meet link to join; `leave`, which is a Boolean flag indicating whether the user wants to automatically leave the meeting after a specified duration; and `durationInMins`, which is the duration of the meeting in minutes. Additionally, `h` and `m` arguments can be provided to indicate the joining time for the meeting.

The program first waits until the specified joining time using the wait function. It then opens a new Chrome browser window by pressing the "win+2" key (you can provide the path to your browser alternately), waits for 5 seconds, and opens the specified Google Meet link in a new tab using the webbrowser library.

The program then turns off the camera and audio by pressing the "ctrl + e" and "ctrl + d" keys, respectively, to ensure that the user's camera and microphone are disabled by default upon joining the meeting.

Next, the program attempts to locate the "Join Now" button on the screen using OpenCV's `locateCenterOnScreen` function. If the button is not found, the program clicks on the "Ask to Join" button instead. If neither button is found, the program continues without joining the meeting.

Once the "Join Now" or "Ask to Join" button is clicked, the program sends an instant WhatsApp message to the user's phone number using the `sendwhatmsg_instantly` function of the PyWhatKit library. This message contains the Google Meet link and the time at which the user joined the meeting.

If the `leave` flag is set to True, the program waits for the specified meeting duration before leaving the meeting. Upon leaving the meeting, the program sends another WhatsApp message to the user's phone number containing the time at which the user left the meeting.

In summary, this program automates the process of joining and leaving Google Meet sessions by performing various tasks automatically. It is designed to save users time and reduce the potential for human error during the meeting joining process.



