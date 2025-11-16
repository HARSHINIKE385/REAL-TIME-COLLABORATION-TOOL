COMPANY NAME : CODTECH IT SOLUTIONS

NAME : HARSHINI.K.E

INTERN ID : CT04DR1003

DOMAIN NAME : SOFTWARE DEVELOPMENT

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH

DESCRIPTION OF THE TASK:

The Collaborative WebSocket Editor is an interactive, real-time code editor that allows multiple users to simultaneously view and edit a shared document over the web. This project leverages WebSockets to establish a persistent connection between clients and the server, enabling instant communication without requiring page reloads. Unlike traditional HTTP requests, which are stateless and require constant polling, WebSockets maintain a continuous, bidirectional channel. This ensures that any change made by one user is immediately reflected on all connected clients, providing a seamless collaborative experience.

At the core of the project is a Python WebSocket server implemented using the websockets library. The server maintains a central DOCUMENT object containing the current text and its version. Whenever a client connects, the server sends the latest state of the document. As users type, their changes are sent as patch messages to the server, which then updates the document and broadcasts the new state to all connected clients. This ensures synchronization while preventing version conflicts. The server is lightweight and can handle multiple clients concurrently, making it ideal for small to medium-sized collaborative applications.

The client side consists of a simple HTML editor with a <textarea> for text input. Using JavaScript, the editor establishes a WebSocket connection to the server and listens for incoming messages. When updates arrive, the editor intelligently applies them, ensuring that typing users are not interrupted. A local version counter tracks the document state to prevent conflicts, and a small delay mechanism ensures smooth typing even when updates are received in rapid succession. This architecture balances real-time collaboration with user experience, avoiding overwriting content mid-typing.

The project is designed to run locally on VS Code, a versatile code editor and development environment. Running the project in VS Code eliminates many limitations associated with cloud-based platforms such as Colab. Users can test the editor on localhost without encountering external dependency issues, and developers can debug, modify, and extend the project directly within the editor. For external access, tools like ngrok v3 can be used to expose the local server to the internet, allowing collaboration across different devices and networks.

This web-based editor has a variety of potential applications. It can be used in educational environments to teach programming collaboratively, in team development settings for real-time code review or pair programming, or even as a lightweight platform for writing and note-taking. Its simplicity and modular design make it adaptable, allowing developers to integrate features like syntax highlighting, user authentication, or advanced version control in future iterations.

In summary, the Collaborative WebSocket Editor combines Python, JavaScript, and HTML to provide a lightweight, responsive, and user-friendly platform for real-time collaboration. Its reliance on WebSockets ensures fast and efficient communication, and its local deployment through VS Code offers flexibility, control, and easy testing for developers and users alike.

OUTPUT SCREENSHOTS:

