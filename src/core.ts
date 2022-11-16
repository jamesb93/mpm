import * as fs from 'fs';

export function validURL(rawUrl: string): boolean {
	let url;
	try {
		url = new URL(rawUrl);
	} catch (err) {
		return false;
	}
	return url.protocol === "http:" || url.protocol === "https:";
}

export function isMaxPackage(path: string): boolean {
	return true
}

export function getMaxPath() {
	
}

export function getLibraryPath() {

}

export function getPackagePath() {

}