<template>
	<q-page padding class="row" dark>
		<div>
			ytuyi
		</div>
	</q-page>
</template>

<script>
import { useQuasar } from 'quasar';

export default {
	name: 'GraphPage',
	setup () {
		const q = useQuasar()
		q.dark.set(true)
	}
}
</script>


<style>
</style>
