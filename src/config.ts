import * as fs from 'fs';
import * as path from 'path';

interface Config {
	library: string[],
}

function getConfig(path: string): Config {
	const configPath = path.join(path, 'mpm.json');
	const config = JSON.parse(fs.readFileSync(path, 'utf8'));
	return config;
}