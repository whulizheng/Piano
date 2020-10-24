import Utils


def select_classifier(classifier_name, input_shape, nb_classes, output_directory):
    if classifier_name == "fcn":
        import Classifier_FCN
        return Classifier_FCN.Classifier_FCN(
            input_shape=input_shape,
            nb_classes=nb_classes,
            output_directory=output_directory
        )


if __name__ == "__main__":
    config = Utils.readjson("config.json")
    classifier = select_classifier(
        config["model"]["model_name"],
        config["model"]["input_shape"],
        config["model"]["nb_classes"],
        config["model"]["model_path"])
    print(config)
