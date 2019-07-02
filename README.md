# hubot-mongo-bridge
Bridge between hubot scripts and Rocket.Chat mongodb

## Settings

You can set up project by using environment variables

<table>
    <tr>
        <th>NAME</th>
        <th>DESCRIPTION</th>
        <th>DEFAULT VALUE</th>
    </tr>
    <tr>
        <td>HOST</td>
        <td>Host name for the server</td>
        <td>localhost</td>
    </tr>
    <tr>
        <td>PORT</td>
        <td>Port number for the server</td>
        <td>8000</td>
    </tr>
    <tr>
        <td>MONGODB_HOST</td>
        <td>MongoDB host where app will connect</td>
        <td>localhost</td>
    </tr>
    <tr>
        <td>MONGODB_PORT</td>
        <td>MongoDB port where app will connect</td>
        <td>27017</td>
    </tr>
</table>

## Install

- `make`

- `docker run -p 8000:8000 --env MONGODB_HOST='your_mongo_host' hubot-mongo-bridge-server`

## Usage

`http://localhost:8000/locale?user_id=foo`
