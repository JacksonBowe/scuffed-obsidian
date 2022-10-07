<template>
  	<div>
		<div ref="container">
			<canvas></canvas>
		</div>
	</div>
</template>

<script>
import { useQuasar } from 'quasar'
import { vis } from 'src/boot/vis'
import { useRoute } from 'vue-router'
import files from '../content/.files.json'

export default {
	name: 'SLocalGraph',
	setup () {
		const q = useQuasar()
		const route = useRoute()
		console.log(route.params)
		const GRAPH_OPTIONS = {
			nodes: {
				shape: "dot",
				color: q.dark ? "#8c8e91" : "#dee2e6",
				font: {
					// face: "Inter",
					size: 16,
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
				solver: "barnesHut",
				repulsion: {
                    centralGravity: 0.6,
                    springLength: 250,
                    springConstant: 0.05,
                    nodeDistance: 200,
                    damping: 0.3
				}
			},
		}

		var nodes = new vis.DataSet([])
		var edges = new vis.DataSet([])

		for (const file of files) {
			// console.log(file)
		}
		return {}
	}
}
</script>
