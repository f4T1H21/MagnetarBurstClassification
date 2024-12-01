import json
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

from Event.Events import Event, EventList, Photon


def read_event(filename, type):
    photons = []
    with open(filename, "r") as f:
        df = pd.read_csv(f)

        time = df.iloc[:, 0].to_numpy()
        energy = df.iloc[:, 1].to_numpy()

        for e, t in zip(energy, time):
            photons.append(Photon(e, t))
    return Event(photons, type, filename)


def plot_features(events_features: dict) -> None:
    # For every frature in existing features
    for i, feature in enumerate(events_features[1].keys()):
        event_ids = [event_id for event_id, features in events_features.items()]
        values = [features[feature] for event_id, features in events_features.items()]
        plt.bar(
            event_ids,  # Bin edges for the x-axis
            values,  # Counts for the y-axis
            width=0.5,
            color="coral",
            edgecolor="black",
        )

        plt.xlabel("Event ID")
        # ylabel = feature
        # if Event.features[feature] != None:
        #     unit = Event.features[feature]
        #     ylabel += f" ({unit})"
        plt.xticks(range(1, len(event_ids) + 1))
        # plt.ylabel(ylabel)
        plt.legend()
        plt.title(f"Comparison of Events based on {feature}")
        plt.show()


if __name__ == "__main__":
    BIN_SIZE = 0.02

    events_list: list[EventList] = []

    for i in range(1, 51):
        main_event = read_event(f"events 2/{i}.csv", "main")
        sb_event = read_event(f"events 2/{i}s.csv", "sb")
        events_list.append(EventList(main_event, sb_event))

    # feature_dict = {}
    for i, events in enumerate(events_list):
        pass
        # events.plot_events_multiple_axes(bin_size=BIN_SIZE)
        # combined = events.combine_events()
        # threshold = combined.compute_threshold()
        # # print(threshold)

        # events.plot_events_multiple_axes(bin_size=BIN_SIZE)
        # # combined.plot_event(bin_size=BIN_SIZE)
        # feature_dict[i + 1] = combined.extract_features()
        # print(json.dumps(combined.features, indent=4))

        # plot_features(events_features=feature_dict)