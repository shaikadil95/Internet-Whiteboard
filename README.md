# Internet-Whiteboard

BRIEF PROJECT DESCRIPTON:  

This is an internet whiteboard application.Upon start, the application will connect to a predefined admin server.
 The IP address of the admin server is configurable, so users can change it at any time. There are three types of user
 accounts: a predefined admin account, employee account and customer accounts. The admin account can create the other 
type of accounts as well as modify critical aspects of the system.
 Employees can create customer accounts, configure and start whiteboard sessions. Customers can join existing sessions. 
When an account is created an e-mail is sent to the owner of the
 account with login details and validity period for the account. The user account is maintained in a SQL DB.

A whiteboard session consists of a set of potentially unlimited number of users (participants) and a set of whiteboard sheets.
 Each user is running the application on their own device. 
A sheet is a display window whose contents are replicated on all devices in real-time. The participants can simultaneously draw and type text
 on the sheets. A set of standard shape drawing tools are  provided: line, arrow, circle, oval, square, rectangle, poly-line, text, eraser 
and free-drawing tool. For each tool, the user is able to select thickness, the drawing 
color and the filling color (just like in other drawing applications). For text, there is no thickness or filling color. Instead, the user 
selects the font, size and optionally a modifier such as italics and/or bold. The users can't undo changes or move shapes, but they can erase.

One of the participants is designated as moderator. By default, this is the creator of the session. However, the creator can assign the moderator 
role to any participant. The moderator can lock access to a sheet (to prevent editing wars), sequentially undo modifications and change to a 
different sheet.

Each modification is saved in a list stored on the admin server (preferably in a DB). The modification data consists of a index, a timestamp, 
the name of user that produced the modification, and the type of modification and on what sheet occurred. After a moderator has locked the 
whiteboard, it can undo modifications. The undo operation retrieves the last change from the list.
 It then redraws the same shape, but all in white so that is indistinguishable from the background. The next undo operations picks the next 
modification from the back of the list. The undo modification are also saved to the modification list (so that participants can see that their
 work has been undone). However, the undo modifications have a special status in the list. They cannot be modified by later undo operations.
 An undo operation always select the latest regular (not undo) operation.

It is possible to save and reload the list of changes. When the list of changes is reloaded the whiteboard is cleared (all sheets). 
Then, a user is able to move sequentially through the modifications by clicking the mouse. For each click, the next modification from the list is
 added to the whiteboard and the modification timestamp and name of user responsible
 for it are shown. It is  also able to playback all modifications automatically by providing a delay between each modification shown.
Certificates areused for each user as well as for the central server hosting the database. Certificates can be self-signed in the release
 to the customer. Encryption features provided by well-known libraries such as OpenSSL/LibreSSL, libcurl or standard Java/Python
 libraries (for example, HttpsURLConnection, httplib.py, ssl.py)  are used. It is possible to restart the system 
with encryption disabled for debugging purposes.

All interaction user-to-user and user-to-server are based on a RESTful API with JSON data encoding. Such an API is  easily testable by using HTTP(S)
 and the command-line utility curl, from the package libcurl.
