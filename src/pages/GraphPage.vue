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
import files from '../content/.files.json'
// import * as vis from "vis-network"
// import * as data from "vis-data"

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min); // The maximum is exclusive and the minimum is inclusive
}


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
				repulsion: {
				centralGravity: 0.2,
				springLength: 200,
				springConstant: 0.05,
				nodeDistance: 100,
				damping: 0.09
				}
			},
		}

		const PASTEL_COLORS = [
			"#FFADAD",
			"#FFD6A5",
			"#FDFFB6",
			"#CAFFBF",
			"#9BF6FF",
			"#A0C4FF",
			"#BDB2FF",
			"#FFC6FF",
			"#FBF8CC",
			"#FDE4CF",
			"#FFCFD2",
			"#F1C0E8",
			"#CFBAF0",
			"#A3C4F3",
			"#90DBF4",
			"#8EECF5",
			"#98F5E1",
			"#B9FBC0",
			"#EAE4E9",
			"#FFF1E6",
			"#FDE2E4",
			"#FAD2E1",
			"#E2ECE9",
			"#BEE1E6",
			"#F0EFEB",
			"#DFE7FD",
			"#CDDAFD",
		]

		console.log('vis2', vis)
		var nodes = new vis.DataSet([])

		var edges = new vis.DataSet([])
		console.log(files)

		for (var file of files) {
			console.log('file', file)
			nodes.add([{
				id: file.id,
				label: file.title,
				size: Math.max(15, Math.min(15 + file.links.length, 30)),
				color: PASTEL_COLORS[Math.floor(Math.random() * PASTEL_COLORS.length)]
			}])
			for (var link of file.links) {
				console.log(link, files.find(e => e.title == link).id)
				edges.add([{
					from: file.id,
					to: files.find(e => e.title == link).id,
					length: getRandomInt(100, 201)
				}])
			}
		}

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
