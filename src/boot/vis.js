import { boot } from 'quasar/wrappers'
import * as network from "vis-network"
import * as data from "vis-data"

// "async" is optional;
// more info on params: https://v2.quasar.dev/quasar-cli/boot-files
export default boot(async (/* { app, router, ... } */) => {
	console.log(Object.assign({}, network, data))
})
