<template>
	<q-page padding class="row" dark>
		<div ref="container">
			<!-- <div> -->
				<canvas width="600" height="600"></canvas>
			<!-- </div> -->
		</div>
	</q-page>
</template>

<script>
import { useQuasar } from 'quasar';
import { vis } from 'src/boot/vis';
import { onMounted, ref } from 'vue';
// import * as vis from "vis-network"
// import * as data from "vis-data"

export default {
	name: 'GraphPage',
	setup () {
		const q = useQuasar()
		q.dark.set(true)

		console.log('vis2', vis)
		var nodes = new vis.DataSet([
			{ id: 1, label: "Node 1" },
			{ id: 2, label: "Node 2" }
		])

		var edges = new vis.DataSet([
			{ from: 1, to: 2 }
		])

		const container = ref(null)
		var data = {
			nodes: nodes,
			edges: edges
		}
		onMounted(() => {
			console.log(container.value)
			// var network = new vis.Network(container.value, data, {})
		})
		//
		console.log(data)


		return {
			container
		}
	}
}
</script>


<style>
</style>
