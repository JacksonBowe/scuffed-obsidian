<template>
  	<!-- <div class="bg-red" style="width: 100%; height: 100%;"> -->
		<div class="col">
			<div ref="container" style="height: 99%">
				<div>
					<canvas></canvas>
				</div>
			</div>
		</div>
</template>

<script>
import { useQuasar } from 'quasar'
import { vis } from 'src/boot/vis'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { DISTINCT_COLORS, PASTEL_COLORS } from '../utils/colors.js';

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min); // The maximum is exclusive and the minimum is inclusive
}

const pointOnCircumference = (radius) => {
    var angle = Math.random() * Math.PI*2; // Random angle
    var x = Math.cos(angle) * radius;
    var y = Math.sin(angle) * radius;
    return [x, y]
}

export default {
	name: 'SGraph',
	props: {
		files: {
			type: Object,
			required: true
		}
	},
	setup (props) {
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

		if (props.files && props.files.length) {


			for (const file of props.files) {
				console.log(file)
				// Add the edges
				for (const link of file.links) {
					// Check if link already exists
					if (edges.get().some(e => e.from == file.id && e.to == props.files.find(e => e.title == link).id)) { continue }
					// Check if backlink already exists
					if (edges.get().some(e => e.to == file.id && e.from == props.files.find(e => e.title == link).id)) { continue }

					// Add new link
					edges.add([{
						from: file.id,
						to: props.files.find(e => e.title == link).id,
						length: getRandomInt(100, 201)
					}])
				}

				let node = {
					id: file.id,
					label: file.title.replace(".md", ''),
					scaling: {
						min: 10,
						max: 30,
						label: {
							enabled: true,
							min: 14,
							max: 30,
							// maxVisible: 30,
							drawThreshold: 10
						}
					},
					mass: 1,
					src: file.src,
					value: (edges.get().filter(e => e.to == file.id)).length + 1,
					color: PASTEL_COLORS[Math.floor(Math.random() * PASTEL_COLORS.length)],
					// opacity: 0.8
				}

				if (!file.links.length) {
					var [x, y] = pointOnCircumference(5000)
					node.value = 1
					node.x = x
					node.y = y
				}

				nodes.add([node])
			}
		}

		const container = ref(null)
		var data = {
			nodes: nodes,
			edges: edges
		}

		onMounted(async () => {
			var network = new vis.Network(container.value, data, GRAPH_OPTIONS)
				.on('selectNode', (p) => {
					let file = props.files.find(x => x.id == p.nodes[0])
					var t = []
					edges.forEach(e => {
						console.log(e.to, file.id)
						if (e.to == file.id) { t.push(e) }
					})
					console.log('edges that reference', t)
					console.log('p', p, props.files.find(x => x.id == p.nodes[0]))
				})
                .on('hoverNode', (p) => {
                    console.log('hovering', p)
					console.log(nodes.get()[p.node])
					nodes.get()[p.node].opacity = 1
                })
		})

		return {
			container
		}
	}
}
</script>
