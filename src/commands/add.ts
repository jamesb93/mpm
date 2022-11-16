import {Command, Flags} from '@oclif/core'
import { validURL, getConfig } from '../core';
import * as fs from 'fs';

export default class Add extends Command {
  static description = 'describe the command here'
  static examples = ['<%= config.bin %> <%= command.id %>']
  static args = [{ name: 'package' }]

  public async run(): Promise<void> {
    const {args, flags} = await this.parse(Add)

    const isURL = validURL(args.package);
    const isDir = fs.lstatSync(args.package).isDirectory() 

    if (isURL) {
    }
    if (isDir) {
      const exists = fs.existsSync(args.package);

      
      // const package = isMaxPackage(args.package)
      // Is it a package?

    }




  }
}
