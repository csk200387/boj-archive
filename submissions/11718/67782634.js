var fs = require('fs');
fs.readFile('/dev/stdin', (err, data) => {
        if (err) {
                console.error(err);
                return
        }
        console.log(data.toString())
})