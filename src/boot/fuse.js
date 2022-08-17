import { boot } from 'quasar/wrappers'
import Fuse from 'fuse.js'
import files from '../content/.search.json'

// var index = elasticlunr(function () {
// 	this.addField('title');
// 	this.addField('body');
// 	this.setRef('id')
// })

const options = {
    // isCaseSensitive: false,
    // includeScore: false,
    // shouldSort: true,
    // includeMatches: false,
    // findAllMatches: false,
    // minMatchCharLength: 1,
    // location: 0,
    // threshold: 0.6,
    // distance: 100,
    // useExtendedSearch: false,
    // ignoreLocation: false,
    // ignoreFieldNorm: false,
    // fieldNormWeight: 1,
    keys: [
      "title",
      "body"
    ]
  };

const fuse = new Fuse(files, options)

// console.log('search', fuse.search('Mafioso'))


export default boot(async ( { app } ) => {
})

export { fuse }
