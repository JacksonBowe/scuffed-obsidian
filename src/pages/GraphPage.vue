<template>
	<q-page padding class="row" dark>

		<s-graph :files="files" />
	</q-page>
</template>

<script>
import { useQuasar } from 'quasar';
import SGraph from 'src/components/SGraph.vue'
import files from '../content/.files.json'



export default {
	name: 'GraphPage',
	components: {
		SGraph
	},
	setup () {
		const q = useQuasar()
		q.dark.set(true)

		return {
			files
		}
	}
}
</script>


<style>
</style>
