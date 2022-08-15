import { boot } from 'quasar/wrappers'
import elasticlunr from 'elasticlunr'
import files from '../content/.search.json'

var index = elasticlunr(function () {
	this.addField('title');
	this.addField('body');
	this.setRef('id')
})


export default boot(async ( { app } ) => {
	files.forEach(file => {
		index.addDoc(file)
	})
})

export { index }
