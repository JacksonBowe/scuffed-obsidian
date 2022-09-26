<template>
	<q-page padding class="row" dark>
		<!-- <div class="bg-red" style="width: 100%; height: 100%;"> -->
		<div class="col">
			<div ref="container" style="height: 99%">
			<!-- <div> -->
				<canvas></canvas>
			<!-- </div> -->
			</div>
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

		const GRAPH_OPTIONS = {
			nodes: {
				shape: "dot",
				color: q.dark ? "#8c8e91" : "#dee2e6",
				font: {
					face: "Inter",
					color: q.dark ? "#c9cdd1" : "#616469",
					strokeColor: q.dark ? "#c9cdd1" : "#616469",
				},
				scaling: {
					label: {
						enabled: true,
					},
				},
			},
			edges: {
				color: { inherit: "both" },
				width: 0.8,
				smooth: {
					type: "continuous",
				},
				hoverWidth: 4,
			},
			interaction: {
				hover: true,
			},
			height: "100%",
			width: "100%",
			physics: {
				solver: "repulsion",
			},
		}

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
			var network = new vis.Network(container.value, data, GRAPH_OPTIONS)
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
