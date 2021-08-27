// Humanoid - UserBot
// Copyright (C) 2020 TeamHumanoid
//
// This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
// PLease read the GNU Affero General Public License in
// <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.

const { exec } = require('child_process');
const { appendFileSync, truncate } = require('fs');

(async () => {
    truncate('./src/ecmaHelper/evalJs.result.d.txt', 0, function() {
        console.log('ResHuman File Truncated')
        const evalJs = exec('node ./src/ecmaHelper/evalJs.run.js');

        evalJs.stdout.on('data', (data) => {
            appendFileSync('./src/ecmaHelper/evalJs.result.d.txt', `${data.toString()}\n`, () => {});
        });

        evalJs.stderr.on('data', (error) => {
            appendFileSync('./src/ecmaHelper/evalJs.result.d.txt', `${error}\n`, () => {});
        });
    });
})();
