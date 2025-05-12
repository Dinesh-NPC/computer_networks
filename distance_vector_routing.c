#include <stdio.h>
struct Router {
    unsigned dist[20];
    unsigned via[20];
} rt[10];
int main() {
    int cost[20][20], nodes, i, j, k, updated;
    printf("\nEnter number of nodes: ");
    scanf("%d", &nodes);
    printf("\nEnter the cost matrix:\n");
    for (i = 0; i < nodes; i++) {
        for (j = 0; j < nodes; j++) {
            scanf("%d", &cost[i][j]);
            cost[i][i] = 0;
            rt[i].dist[j] = cost[i][j];
            rt[i].via[j] = j;
        }
    }
    do {
        updated = 0;
        for (i = 0; i < nodes; i++) {
            for (j = 0; j < nodes; j++) {
                for (k = 0; k < nodes; k++) {
                    if (rt[i].dist[j] > cost[i][k] + rt[k].dist[j]) {
                        rt[i].dist[j] = cost[i][k] + rt[k].dist[j];
                        rt[i].via[j] = k;
                        updated++;
                    }
                }
            }
        }
    } while (updated != 0);
    for (i = 0; i < nodes; i++) {
        printf("\nRouting Table for Router %d:\n", i + 1);
        printf("Destination\tDistance\tNext Hop\n");
        printf("-----------------------------------\n");
        for (j = 0; j < nodes; j++) {
            printf("%d\t\t%d\t\t%d\n", j + 1, rt[i].dist[j], rt[i].via[j] + 1);
        }
    }
    return 0;
}
