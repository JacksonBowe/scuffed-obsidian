<template>
	<q-page padding class="row" dark>
		<div>
			ytuyi
		</div>
	</q-page>
</template>

<script>
import { useQuasar } from 'quasar';
// import * as vis from "vis-network"
// import * as data from "vis-data"

export default {
	name: 'GraphPage',
	setup () {
		const q = useQuasar()
		q.dark.set(true)
		// console.log(data)
	}
}
</script>


<style>
</style>
