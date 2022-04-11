# Simple Python Proxy

The simple python proxy uses the low-level `socket` modules included in the python built-in modules.

It is an interesting concept that teaches the interaction between the web-browser and server. It could also be used as a custom tool to read packets from any type of server given the correct implementation.

## Standard Socket Connection Diagram (Server / Client)

| SERVER | CLIENT|
|--------|-------|
|socket| socket |
|bind | |
|listen| |
|accept| connect |
|recv | send|
|send| recv|
