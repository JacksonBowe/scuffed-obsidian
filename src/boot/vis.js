import { boot } from 'quasar/wrappers'
import * as network from "vis-network"
import * as data from "vis-data"

console.log('data', data)

const vis = Object.assign({}, network, data)


export default boot(async (/* { app, router, ... } */) => {
	console.log('vis', vis)
	return vis
})

export { vis }

