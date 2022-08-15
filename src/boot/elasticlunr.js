import { boot } from 'quasar/wrappers'
import elasticlunr from 'elasticlunr'

var index = elasticlunr(function () {
    this.addField('title');
    this.addField('body');
    this.setRef('id')
})

export default boot(async ( { app } ) => {
  // something to do
})
